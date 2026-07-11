%global tl_name collection-formatsextra
%global tl_revision 72250

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Additional formats
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-formatsextra
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-formatsextra.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(aleph)
Requires:	texlive(antomega)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Requires:	texlive(eplain)
Requires:	texlive(hitex)
Requires:	texlive(jadetex)
Requires:	texlive(lambda)
Requires:	texlive(lollipop)
Requires:	texlive(mltex)
Requires:	texlive(mxedruli)
Requires:	texlive(omega)
Requires:	texlive(omegaware)
Requires:	texlive(otibet)
Requires:	texlive(passivetex)
Requires:	texlive(psizzl)
Requires:	texlive(startex)
Requires:	texlive(texsis)
Requires:	texlive(xmltex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Collected TeX `formats', i.e., large-scale macro packages designed to be
dumped into .fmt files -- excluding the most common ones, such as latex
and context, which have their own package(s). It also includes the Aleph
engine and related Omega formats and packages, and the HiTeX engine and
related.

