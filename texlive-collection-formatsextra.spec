# revision 33658
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-formatsextra
Epoch:		1
Version:	20190228
Release:	1
Summary:	Additional formats
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-formatsextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-edmac
Requires:	texlive-eplain
Requires:	texlive-lollipop
Requires:	texlive-mltex
Requires:	texlive-psizzl
Requires:	texlive-startex
Requires:	texlive-texsis

%description
Collected TeX `formats', i.e., large-scale macro packages
designed to be dumped into .fmt files -- excluding the most
common ones, such as latex and context, which have their own
package(s).

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
