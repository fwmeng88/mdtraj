##############################################################################
# MDTraj: A Python Library for Loading, Saving, and Manipulating
#         Molecular Dynamics Trajectories.
# Copyright 2012-2013 Stanford University and the Authors
#
# Authors: Robert McGibbon
# Contributors:
#
# MDTraj is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Foobar. If not, see <http://www.gnu.org/licenses/>.
##############################################################################


"""The mdtraj package contains tools for loading and saving molecular dynamics
trajectories in a variety of formats, including Gromacs XTC & TRR, CHARMM/NAMD
DCD, AMBER BINPOS, PDB, and HDF5.
"""

from __future__ import print_function, division
from mdtraj.xtc import XTCTrajectoryFile
from mdtraj.trr import TRRTrajectoryFile
from mdtraj.hdf5 import HDF5TrajectoryFile
from mdtraj.netcdf import NetCDFTrajectoryFile
from mdtraj.mdcrd import MDCRDTrajectoryFile
from mdtraj.dcd import DCDTrajectoryFile
from mdtraj.binpos import BINPOSTrajectoryFile
from mdtraj.pdb import PDBTrajectoryFile
from mdtraj.arc import ArcTrajectoryFile

from mdtraj.rmsd import rmsd_cache
from mdtraj.topology import Topology
from mdtraj.geometry import *
from mdtraj.trajectory import *

def test(label='full', verbose=2):
    """Run tests for mdtraj using nose.

    Parameters
    ----------
    label : {'fast', 'full'}
        Identifies the tests to run. The fast tests take about 10 seconds,
        and the full test suite takes about two minutes (as of this writing).
    verbose : int, optional
        Verbosity value for test outputs, in the range 1-10. Default is 2.
    """
    import mdtraj
    from mdtraj.testing.nosetester import MDTrajTester
    tester = MDTrajTester(mdtraj)
    return tester.test(label=label, verbose=verbose, extra_argv=('--exe',))
# prevent nose from discovering this function, or otherwise when its run
# the test suite in an infinite loop
test.__test__ = False
