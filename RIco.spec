%global	_prefix	/opt
%global	packdir	RIco

Name:		RIco
Version:	1.0.7
Release:	5%{?dist}
Summary:	Package for the 3D Reconstruction of Icosahedral objects

Group:          Applications/Engineering
License:        Public Domain
URL:            https://sites.google.com/site/downloadrico/home
Source0:        %{name}Dist-%{version}.tgz
Source1:	%{name}BIN_linux_x86_32_gfortran_static-%{version}.tar
Patch0:		%{name}-startup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Would be lesstif on Fedora
Requires:       lesstif >= 0.95.2
Requires:	ncurses
Requires:	gnuplot
Requires:	vim-enhanced
Requires:	ImageMagick
#Requires:	fftw3
#Requires:	libgfortran44

%description
The 3D Cryo-Electron Microscopy (3D cryo-EM) is a method for the
structure determination of (biological) macromolecules. Besides
experimental techniques, 3D cryo-EM depends on special software
(e.g. RIco) to produce medium resolution 3D maps (50Å-10Å) from a set
of 2D images produced by an electron microscope.

Many viruses are knwon to have icosahedral capsids to carry and
protect their genetic material. Therefore, the presence of symmetry
can be exploited allowing effective information extraction.

RIco uses Symmetry Adapted Functions (SAFs) to extract maximum
information from a minimum quantity of images.

%prep
%setup -q -n %{name}Dist
%patch0 -p1 -b .%{name}-startup.patch

tar xvf %{SOURCE1} --strip-components=1

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_prefix}/%{packdir}/
#mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

#TODO: world write permissions on test_data
#world execute permissions on BIN* directory

#cp README Navaza2003.pdf %{buildroot}%{_docdir}/%{name}-%{version}
mv  * %{buildroot}%{_prefix}/%{packdir}/

#needed to run tests
chmod -R 777 %{buildroot}%{_prefix}/%{packdir}/test_data

#fix binary permissions
chmod 0755 %{buildroot}%{_prefix}/%{packdir}/BIN_linux_x86_32_gfortran_static/*


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_prefix}/%{packdir}
%{_prefix}/%{packdir}/*



%changelog
* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-5
- fix permissions for binaries and test_data

* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-4
- use -static instead of -dynamic, because of missing libgfortran version

* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-3
- ensure specific binary files included

* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-2
- add explicit reqs. for lesstif, for EPEL5
- add other explicit reqs
- fix ownership of main directory
- add patch for startup.tcsh

* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-1
- initial version

