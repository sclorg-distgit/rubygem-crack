%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name crack

Summary: Really simple JSON and XML parsing, ripped from Merb and Rails
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jnunemaker/crack
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(safe_yaml) >= 1.0.0
Requires: %{?scl_prefix}rubygem(safe_yaml) < 1.1
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(safe_yaml)
BuildArch: noarch
#BZ 781829
Epoch: 1
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Really simple JSON and XML parsing, ripped from Merb and Rails.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Fix non-standard-executable-perm rpmlint warning.
chmod a+x %{buildroot}%{gem_instdir}/script/*

%check 
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/crack.gemspec
%{gem_instdir}/script
%{gem_instdir}/test

%changelog
* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 1:0.4.2-4
- Add missing dependency on safe_yaml

* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 1:0.4.2-3
- Add missing provides

* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 1:0.4.2-2
- Add SCL macros

* Mon Jul 14 2014 Vít Ondruch <vondruch@redhat.com> - 1:0.4.2-1
- Update to crack 0.4.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1:0.3.2-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to crack 0.3.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.3.1-3
- Properly require the main package (with epoch) from the -doc subpackage.

* Wed Mar 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.3.1-2
- Update to 0.3.1

* Sun Feb 05 2012 <stahnma@fedoraproject.org> - 0.1.8-5
- Revert back to 0.1.8 as HTTParty can't use crack > 0.1.8

* Wed Dec 28 2011 <stahnma@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1
- Fix bz #715704

* Thu Nov 10 2011 Michael Stahnke <mastahnke@gmail.com> - 0.1.8-3
- rebuilt

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.1.8-1
- Broke package into main and doc
- Added tests
