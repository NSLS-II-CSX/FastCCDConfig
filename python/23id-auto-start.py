#! /usr/bin/python
# -*- coding: utf-8 -*-

import cin_constants
import cin_register_map
import cin_functions
import time

# Power Cycle CIN to clear stale configurations
cin_functions.CINPowerDown()
cin_functions.CINPowerUp()

import getCfgFPGAStatus

# Configure Frame FPGA
cin_functions.loadFrmFirmware("/home/swilkins/Repos/FastCCDConfig/binary/top_frame_fpga.bit")

import getFrmFPGAStatus
#import setFClk200M
import getFClkStatus

#Load Camera Timing File for 23ID Camera System
#cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/23ID_FS_NOS_200MHz_CCD_timing.txt")
#cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/23ID_FS_2OS_200MHz_CCD_timing.txt")
#cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/archive/2014_Jan_21-CCD_timing_200MHz.txt")
#cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/archive/2013_Nov_30-09_28_CCD_timing_200MHz.txt")
cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/2014_Jan_07-07_31_CCD_23ID_FS.txt")

#print "\nSet Trigger Mux
#import setTrigger0   # Maps to Front Panel Trigger Input 1
import setTriggerSW

#Set Exposure Time to 20us here with a cin_functions writeReg()
cin_functions.WriteReg("8206", "0000", 1)  # MS Byte
cin_functions.WriteReg("8207", "0001", 1)  # LS Byte
#Set Num Exposures == 1
cin_functions.WriteReg("820C", "0001", 1)
#Set Repitition Rate for SW triggers
cin_functions.WriteReg("8208", "0000", 1)  # MS Byte
cin_functions.WriteReg("8209", "0032", 1)  # LS Byte

# Power up Front Panel boards
import setFPPowerOn
time.sleep(0.2)  # Wait to allow visual check

#  Send Destination IP address 10.23.5.127
cin_functions.WriteReg("8013", "057F", 1)  # MS Byte
cin_functions.WriteReg("8014", "0A17", 1)  # MS Byte

#  Send UDP packet to configure Stream Port
#print "\nConfigure CIN for Broadcast Mode Tx"
import sendConnect

#raw_input("\n(Press Enter Key to send Bias Configuration to Camera clock board)")

cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/2014_Mar_27-1kFS_Bias_Settings.txt")

#raw_input("\n(Press Enter Key to send FCRIC Configurations)")

cin_functions.loadCameraConfigFile("/home/swilkins/Repos/FastCCDConfig/timing/2013_Nov_25-200MHz_fCRIC_timing.txt")

#./setReg.py 8212 00e0 Mask the bad signal lines FCRIC to CIN
#cin_functions.WriteReg("8211", "FFFF", 1)
#cin_functions.WriteReg("8212", "FFFF", 1)
#cin_functions.WriteReg("8213", "FFFF", 1)

#raw_input("\nfCCD Camera configured and ready to enable (Press Enter Key to Exit)")

