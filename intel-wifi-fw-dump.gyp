{
  'targets': [
    {
      'target_name': 'iwlwifi_dump_processor',
      'type': 'executable',
      'variables': {
        'deps': [
          'libbrillo-<(libbase_ver)',
          'libchrome-<(libbase_ver)',
          'libminijail',
        ],
      },
      'sources': [
        'sandbox/iwlwifi_dump_processor.cc',
      ],
    },
  ],
}
