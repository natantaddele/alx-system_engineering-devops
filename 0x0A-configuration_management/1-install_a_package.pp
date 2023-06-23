# Install puppet-lint
package { 'puppet-lint':
  ensure   => '3.8.10',
  provider => 'gem'
}
