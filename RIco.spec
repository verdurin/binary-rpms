%global	_prefix	/opt
%global	packdir	RIco

Name:		RIco
Version:	1.0.7
Release:	1%{?dist}
Summary:	Package for the 3D Reconstruction of Icosahedral objects

Group:          Applications/Engineering
License:        Public Domain
URL:            https://sites.google.com/site/downloadrico/home
Source0:        %{name}Dist-%{version}.tgz
Source1:	%{name}BIN_linux_x86_32_gfortran_dynamic-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#May need lesstif
#Requires:       

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


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_prefix}/%{packdir}/
#mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

#cp README Navaza2003.pdf %{buildroot}%{_docdir}/%{name}-%{version}
mv  * %{buildroot}%{_prefix}/%{packdir}/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_prefix}/%{packdir}/*



%changelog
* Thu Oct 20 2011 Adam Huffman <bloch@verdurin.com> - 1.0.7-1
- initial version
