# ----------------------------------------------------------------------------
# Copyright (c) 2013--, scikit-bio development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

import unittest

from skbio.metadata._mixin import (MetadataMixin, PositionalMetadataMixin)
from skbio.util._decorator import overrides
from skbio.util._testing import ReallyEqualMixin
from skbio.metadata._testing import (MetadataMixinTests,
                                     PositionalMetadataMixinTests)


class TestMetadataMixin(unittest.TestCase, ReallyEqualMixin,
                        MetadataMixinTests):
    def setUp(self):
        class ExampleMetadataMixin(MetadataMixin):
            def __init__(self, metadata=None):
                MetadataMixin._init_(self, metadata=metadata)

            def __eq__(self, other):
                return MetadataMixin._eq_(self, other)

            def __ne__(self, other):
                return MetadataMixin._ne_(self, other)

            def __copy__(self):
                copy = self.__class__(metadata=None)
                copy._metadata = MetadataMixin._copy_(self)
                return copy

            def __deepcopy__(self, memo):
                copy = self.__class__(metadata=None)
                copy._metadata = MetadataMixin._deepcopy_(self, memo)
                return copy

        self._metadata_constructor_ = ExampleMetadataMixin


class TestPositionalMetadataMixin(unittest.TestCase, ReallyEqualMixin,
                                  PositionalMetadataMixinTests):
    def setUp(self):
        class ExamplePositionalMetadataMixin(PositionalMetadataMixin):
            @overrides(PositionalMetadataMixin)
            def _positional_metadata_axis_len_(self):
                return self._axis_len

            def __init__(self, axis_len, positional_metadata=None):
                self._axis_len = axis_len

                PositionalMetadataMixin._init_(
                    self, positional_metadata=positional_metadata)

            def __eq__(self, other):
                return PositionalMetadataMixin._eq_(self, other)

            def __ne__(self, other):
                return PositionalMetadataMixin._ne_(self, other)

            def __copy__(self):
                copy = self.__class__(self._axis_len, positional_metadata=None)
                copy._positional_metadata = \
                    PositionalMetadataMixin._copy_(self)
                return copy

            def __deepcopy__(self, memo):
                copy = self.__class__(self._axis_len, positional_metadata=None)
                copy._positional_metadata = \
                    PositionalMetadataMixin._deepcopy_(self, memo)
                return copy

        self._positional_metadata_constructor_ = ExamplePositionalMetadataMixin
