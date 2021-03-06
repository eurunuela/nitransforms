# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""
Read and write transforms.

.. currentmodule:: nitransforms.io

.. autosummary::
   :toctree: ../generated

   io

"""
from . import afni, fsl, itk, lta
from .lta import LinearTransform, LinearTransformArray, VolumeGeometry


__all__ = [
    "afni",
    "fsl",
    "itk",
    "lta",
    "LinearTransform",
    "LinearTransformArray",
    "VolumeGeometry",
]
