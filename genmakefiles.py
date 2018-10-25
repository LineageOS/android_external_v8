#!/usr/bin/env python

import os
import subprocess

# Reformat the specified Android.bp file
def _bpFmt(filename):
  subprocess.check_call(["bpfmt", "-w", filename])

def _bpList(name, entries):
  return name + ': [' + ",".join(['"' + x + '"' for x in entries]) + '],\n'

# Given a list of source files from the V8 gyp file, create a string that can
# be put into the bp srcs list. One per line, and with the 'src' directory
# prepended.
def _bpSources(src_list):
  return _bpList('srcs', ['src/' + x for x in src_list])

# Return a string that contains the common header used by the V8 bp files.
def _bpCommonHeader():
  result = ""
  result += '// GENERATED, do not edit\n'
  result += '// for changes, see genmakefiles.py\n'
  return result

# Return a string that contains the common module header.
def _bpModuleHeader(module_type, module_name):
  result = ""
  result += module_type + ' {\n'
  result += 'name: "' + module_name + '",\n'
  result += 'defaults: ["v8_defaults"],\n'
  return result

# Write an Android.bp in the simpler format used by v8_libplatform and
# v8_libsampler
def _writeBP(filename, module_name, sources):
  if not sources:
    raise ValueError('No sources for ' + filename)

  with open(filename, 'w') as out:
    out.write(_bpCommonHeader())
    out.write(_bpModuleHeader("cc_library_static", module_name))
    out.write(_bpSources(sources))
    out.write(_bpList('local_include_dirs', ['src', 'include']))
    out.write('}\n')

  _bpFmt(filename)

def _writeMkpeepholeBP(target):
  if not target:
    raise ValueError('Must specify mkpeephole target properties')

  filename = 'Android.mkpeephole.bp'
  with open(filename, 'w') as out:
    out.write(_bpCommonHeader())

    out.write(_bpModuleHeader('cc_binary_host', 'v8mkpeephole'))

    sources = [x for x in target['sources'] if x.endswith('.cc')]
    sources.sort()
    out.write(_bpSources(sources))

    out.write(_bpList('static_libs', ['libv8base', 'liblog']))
    out.write('}\n')

  _bpFmt(filename)

def _writeV8SrcBP(target):
  if not target:
    raise ValueError('Must specify v8_base target properties')

  filename = 'Android.v8.bp'
  with open(filename, 'w') as out:
    out.write(_bpCommonHeader())
    out.write(_bpModuleHeader('cc_library_static', 'libv8src'))

    sources = [x for x in target['sources'] if x.endswith('.cc')]
    sources = list(set(sources))
    sources.sort()

    out.write(_bpSources(sources))

    arm_src = None
    arm64_src = None
    x86_src = None
    x86_64_src = None
    mips_src = None
    mips64_src = None
    for condition in target['conditions']:
      if condition[0] == 'v8_target_arch=="arm"':
        arm_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]
      elif condition[0] == 'v8_target_arch=="arm64"':
        arm64_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]
      elif condition[0] == 'v8_target_arch=="ia32"':
        x86_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]
      elif condition[0] \
          == 'v8_target_arch=="mips" or v8_target_arch=="mipsel"':
        mips_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]
      elif condition[0] \
          == 'v8_target_arch=="mips64" or v8_target_arch=="mips64el"':
        mips64_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]
      elif condition[0] == 'v8_target_arch=="x64"':
        x86_64_src = [x for x in condition[1]['sources'] if x.endswith('.cc')]

    arm_src.sort()
    arm64_src.sort()
    x86_src.sort()
    x86_64_src.sort()
    mips_src.sort()
    mips64_src.sort()

    out.write('arch: {\n')
    out.write('arm: {\n')
    out.write(_bpSources(arm_src))
    out.write('},\n')
    out.write('arm64: {\n')
    out.write(_bpSources(arm64_src))
    out.write('},\n')
    out.write('mips: {\n')
    out.write(_bpSources(mips_src))
    out.write('},\n')
    out.write('mips64: {\n')
    out.write(_bpSources(mips64_src))
    out.write('},\n')
    out.write('x86: {\n')
    out.write(_bpSources(x86_src))
    out.write('},\n')
    out.write('x86_64: {\n')
    out.write(_bpSources(x86_64_src))
    out.write('},\n')
    out.write('},\n')

    out.write(_bpList('local_include_dirs', ['src']))
    out.write(_bpList('include_dirs', ['external/icu/icu4c/source/common', 'external/icu/icu4c/source/i18n']))
    out.write('}\n')

  _bpFmt(filename)

def _writeGeneratedFilesBP(target):
  if not target:
    raise ValueError('Must specify j2sc target properties')

  filename = 'Android.v8gen.bp'
  with open(filename, 'w') as out:
    out.write(_bpCommonHeader())

    out.write('filegroup {\n')
    out.write('name: "v8_js_lib_files",\n')
    out.write(_bpSources(target['variables']['library_files']))
    out.write('}\n')

    out.write('filegroup {\n')
    out.write('name: "v8_js_experimental_lib_files",\n')
    out.write(_bpSources(target['variables']['experimental_library_files']))
    out.write('}\n')

  _bpFmt(filename)

def _writeLibBaseBP(target):
  if not target:
    raise ValueError('Must specify v8_libbase target properties')

  filename = 'Android.base.bp'
  with open(filename, 'w') as out:
    out.write(_bpCommonHeader())
    out.write(_bpModuleHeader('cc_library_static', 'libv8base'))
    out.write('host_supported: true,\n')

    sources = [x for x in target['sources'] if x.endswith('.cc')]
    sources += ['base/platform/platform-posix.cc']
    sources.sort()

    out.write(_bpSources(sources))

    out.write('local_include_dirs: ["src"],\n')

    out.write('target: {\n')
    out.write('android: {\n')
    out.write(_bpSources(['base/debug/stack_trace_android.cc']))
    out.write('},\n')
    out.write('linux: {\n')
    out.write(_bpSources(['base/platform/platform-linux.cc']))
    out.write('},\n')
    out.write('host: {\n')
    out.write(_bpSources(['base/debug/stack_trace_posix.cc']))
    out.write('},\n')
    out.write('darwin: {\n')
    out.write(_bpSources(['base/platform/platform-macos.cc']))
    out.write('},\n')
    out.write('},\n')

    out.write('}\n')

  _bpFmt(filename)

def GenerateMakefiles():
  # Slurp in the content of the V8 gyp file.
  with open(os.path.join(os.getcwd(), './src/v8.gyp'), 'r') as f:
    gyp = eval(f.read())

  # Find the targets that we're interested in and write out the Android.bps.
  for target in gyp['targets']:
    name = target['target_name']
    sources = None
    if target.get('sources'):
      sources = [x for x in target['sources'] if x.endswith('.cc')]
      sources.sort()

    if name == 'v8_libplatform':
      _writeBP('Android.platform.bp', 'libv8platform', sources)
    elif name == 'v8_libsampler':
      _writeBP('Android.sampler.bp', 'libv8sampler', sources)
    elif name == 'v8_base':
      _writeV8SrcBP(target)
    elif name == 'mkpeephole':
      _writeMkpeepholeBP(target)
    elif name == 'js2c':
      _writeGeneratedFilesBP(target)
    elif name == 'v8_libbase':
      _writeLibBaseBP(target)

if __name__ == '__main__':
  GenerateMakefiles()
