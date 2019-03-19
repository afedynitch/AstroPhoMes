import unittest

import numpy as np
import sys
sys.path.append('../lib/')

from photomeson_models import *
    

class Test_SuperpositionModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_SuperpositionModel, self).__init__(*args, **kwargs)
        
        # creating class instance for testing
        self.pm = SuperpositionModel()

    def test_nonel_nucleons(self):
        """
            Test that nonel works
        """
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid
        
        e, cs = self.pm.cs_nonel(101)
        self.assertTrue(np.all(cs == cs_proton))
        
        e, cs = self.pm.cs_nonel(100)
        self.assertTrue(np.all(cs == cs_neutron))

    def test_nonel_nuclei(self):
        """
            Test that nonel works
        """
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid
        
        e, cs = self.pm.cs_nonel(1406)
        cs_mix = 6 * cs_proton + 8 * cs_neutron
        self.assertTrue(np.all(cs == cs_mix))

    def test_incl_nucleons(self):
        """
            Test that nonel works
        """
        from scipy.integrate import trapz
        
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid

        redist_p = self.pm.redist_proton
        redist_n = self.pm.redist_neutron

        for spec, cs_tot, redist in zip([100, 101], 
            [cs_neutron, cs_proton],
            [redist_n, redist_p]):
            for prod in [2, 3, 4, 100, 101]:
                e, cs = self.pm.cs_incl(spec, prod)
                cs_val_diff = cs_tot * redist[prod].T

                cs_val = trapz(cs_val_diff, x=self.pm.xcenters,
                              dx=bin_widths(self.pm.xbins), axis=0)

                self.assertTrue(np.all(cs == cs_val))        

    def test_incl(self):
        """
            Test that nonel works
        """
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid

        e, cs = self.pm.cs_incl(502, 402)
        cs_val = 3 * cs_neutron
        self.assertTrue(np.all(cs == cs_val))        
                
        e, cs = self.pm.cs_incl(704, 603)
        cs_val = 4 * cs_proton
        self.assertTrue(np.all(cs == cs_val))
        
        e, cs = self.pm.cs_incl(1407, 402)
        cs_val = np.zeros_like(cs)
        self.assertTrue(np.all(cs == cs_val))        

    def test_incl_diff_nucleons(self):
        """
            Test that nonel works
        """
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid

        redist_p = self.pm.redist_proton
        redist_n = self.pm.redist_neutron

        for spec, cs_tot, redist in zip([100, 101], 
            [cs_neutron, cs_proton],
            [redist_n, redist_p]):
            for prod in [2, 3, 4, 100, 101]:
                e, cs = self.pm.cs_incl_diff(spec, prod)
                cs_val = cs_tot * redist[prod].T
                self.assertTrue(np.all(cs == cs_val))        

    def test_incl_diff_nuclei(self):
        """
            Test that nonel works
        """
        cs_proton = self.pm.cs_proton_grid
        cs_neutron = self.pm.cs_neutron_grid
    
        e, cs = self.pm.cs_incl_diff(1407, 100)
        cs_val = 7 * cs_neutron * self.pm.redist_neutron[100].T + \
                 7 * cs_proton * self.pm.redist_proton[100].T
        self.assertTrue(np.all(cs == cs_val))

        e, cs = self.pm.cs_incl(4018, 100)
        cs_val = np.zeros_like(self.pm.cs_proton_grid)

        self.assertTrue(np.all(cs.shape == cs_val.shape))

        e, cs = self.pm.cs_incl_diff(1407, 402)
        cs_val = np.zeros_like(self.pm.redist_proton[2].T)
        self.assertTrue(np.all(cs == cs_val))


# class Test_EmpiricalModel(Test_SuperpositionModel):
#     def __init__(self, *args, **kwargs):
#         super(Test_EmpiricalModel, self).__init__(*args, **kwargs)
        
#         # creating class instance for testing
#         self.pm = EmpiricalModel()

#     def test_nonel_nuclei(self):
#         """
#             Test that nonel works
#         """
#         cs_proton = self.pm.cs_proton_grid
#         cs_neutron = self.pm.cs_neutron_grid
        
#         e, cs = self.pm.cs_nonel(1406)
#         cs_mix = 6 * cs_proton + 8 * cs_neutron
#         self.assertTrue(np.all(cs != cs_mix))


if __name__ == '__main__':
    unittest.main()