#! /usr/bin/python
# -*- coding: utf-8 -*-
import cin_constants
import cin_register_map
import cin_functions

cin_functions.WriteReg (cin_register_map.REG_BIASCONFIGREGISTER0_REG, "0000", 0 )
cin_functions.WriteReg (cin_register_map.REG_CLOCKCONFIGREGISTER0_REG, "0000", 0 )
