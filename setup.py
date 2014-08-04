from distutils.core import setup, Extension

nist5_hash_module = Extension('nist5_hash',
                               sources = ['nist5module.c',
                                          'nist5.c',
										  'sha3/blake.c',
										  'sha3/groestl.c',
										  'sha3/skein.c',
										  'sha3/jh.c',
										  'sha3/keccak.c'],

                               include_dirs=['.', './sha3'])

setup (name = 'nist5_hash',
       version = '1.0',
       description = 'NIST5 Hashing Module For Python',
       ext_modules = [nist5_hash_module])
