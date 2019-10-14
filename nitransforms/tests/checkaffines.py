"""Utilities for testing."""
from pathlib import Path
import numpy as np

from .. import linear as nbl


def assert_affines_by_filename(affine1, affine2):
    """Check affines by filename."""
    affine1 = Path(affine1)
    affine2 = Path(affine2)
    assert affine1.suffix == affine2.suffix, 'affines of different type'

    if affine1.suffix.endswith('.tfm'):  # An ITK transform
        xfm1 = nbl.load(str(affine1), fmt='itk')
        xfm2 = nbl.load(str(affine2), fmt='itk')
        assert xfm1 == xfm2
    else:
        xfm1 = np.loadtxt(str(affine1))
        xfm2 = np.loadtxt(str(affine2))
        np.testing.assert_almost_equal(xfm1, xfm2)
