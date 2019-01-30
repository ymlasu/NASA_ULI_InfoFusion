#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NATIONAL AIRSPACE TRAJECTORY-PREDICTION SYSTEM (NATS)
          Copyright 2018 by Optimal Synthesis Inc. All rights reserved

Author: Jun Yang

Date: 2018-01-19

#Revision Logs
03/21/2018, Added AirportLayout,Node,Link classes to handle airport layout display
and taxi route design.

03/26/2018
Added TaxiPlan class in order to handle plotting and analyzing taxi plans.

"""


import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import h5py
import re
import os
import time
import pickle
import copy


class OutFileHandler:
    """
    This class is to aid parsing the trajectories from output files. This
    supports. The supported file formats include: xml, h5, csv.
    Each trajectory is read into an instance of ACTrajectory.

    """

    #for plotting purpose
    #lat_min=10.78;lat_max=51.28;lon_min=-150;lon_max=-45.25


    def __init__(self):
        """
       Initialize as a place holder.
       Reading output file is done by calling read_xml_file.
        """
        self.callsign_list=[]
        self.traj_list=[]

    @staticmethod
    def get_column_defintion():
        """
        This function returns the definition of column as a python dict variable.


        :return: column defintions for numpy array inside ACTrajectory instance. ACtrajectory.colmap
        """
        return ACTrajectory.colmap

    def get_all_callsigns(self):
        """
        functions to get all the callsigns included in the output file

        :return: list of callsign(strings)
        """
        return self.callsign_list


    def get_callsigns_departing_from(self,org_arpt):
        """
        function to get callsigns departing from the airport given as an airport argument

        :param org_arpt:  origin airport name
        :return: list of callsigns departing from the given origin airport
        """

        callsigns = []
        for ii in range(len(self.callsign_list)):
            if self.traj_list[ii].get_origin_airport() == org_arpt:
                callsigns.append(self.callsign_list[ii])

        return callsigns

    def get_callsigns_arriving_at(self,dest_arpt):
        """
        function to get call signs arrivaing at the given airport

        :param dest_arpt: destination airport (name string)
        :return: list of call signs that arrive at the airport
        """

        callsigns = []
        for ii in range(len(self.callsign_list)):
            if self.traj_list[ii].get_destination_airport() == dest_arpt:
                callsigns.append(self.callsign_list[ii])

        return callsigns

    def get_all_trajectories(self):
        """
        get the list of ACtrajectory instances

        :return: list of ACtrajectory instances
        """
        return self.traj_list

    def get_trajectories_departing_from(self,org_arpt):
        """
        function to get the list of ACTrajectory instances departing from the origin airport

        :param org_arpt: origin airport name
        :return: list of ACTrajectory instances
        """

        cs_list=self.get_callsigns_departing_from(org_arpt)
        return self.get_trajectories_from_callsign_list(cs_list)


    def get_trajectories_arriving_at(self,dest_arpt):
        """
        function to get the list of ACTrajectory instances arriving at the destination airport

        :param dest_arpt: the name of the destination airport
        :return: list of ACTrajectory instances
        """

        cs_list = self.get_callsigns_arriving_at(dest_arpt)
        return self.get_trajectories_from_callsign_list(cs_list)


    def get_trajectories_from_callsign_list(self,callsign_list):
        """
        Given list of call signs, returns the list of ACTrajectory instances

        :param callsign_list: list of call sign strings
        :return: list of ACTrajectory instances
        """

        return [self.get_trajectory_of(callsign) for callsign in callsign_list]

    def get_callsigns_from_to_airports(self,orig_arpt,dest_arpt):
        """
        Given origin & destination airport pairs, return the list of callsigns that depart from the origin
        and arrive at the destination

        :param orig_arpt: the name of the origin airport
        :param dest_arpt: the name of the destination airport
        :return: list of call signs
        """

        org_arpt_list = self.get_callsigns_departing_from(orig_arpt)
        dest_arpt_list = self.get_callsigns_arriving_at(dest_arpt)
        return [callsign for callsign in org_arpt_list if callsign in dest_arpt_list]

    def get_trajectories_from_to_airpots(self,orig_arpt,dest_arpt):
        """
         Given origin & destination airport pairs, return the list of ACTrajectory instances that depart from the origin and arrive at the destination

        :param orig_arpt: the name of the origin airport
        :param dest_arpt: the name of the destination airport
        :return: list of ACTrajectories
        """

        cs_list = self.get_callsigns_from_to_airports(orig_arpt,dest_arpt)
        return self.get_trajectories_from_callsign_list(cs_list)


    def get_trajectory_of(self,callsign):
        """
        Given call sign, return the correponding ACTrajectory instance

        :param callsign: the call sign (string)
        :return:  ACTrajectory instance
        """

        rtn_traj=None
        if callsign in self.callsign_list:
            cs_idx=self.callsign_list.index(callsign)
            rtn_traj=self.traj_list[cs_idx]
        else:
            raise ValueError("callsign:{} is not found in stored trajectories".format(callsign))

        return rtn_traj


    def plot_trajectories_from_callsigns(self,callsigns, plt,color=None,legend=False):
        """
        Plot trajectories specified by callsigns. If the color is specified, all the trajectories are plotted using
        the same color. Otherwise, default colors are used.
        The legend is off in default, if it is True, the legend is displayed with labels as call signs.

        :param callsigns: list of call signs
        :param plt:  matplotlib.pyplot instance (needed to call plot functions)
        :param color: color specification ex)'b'
        :param legend: True or False for displaying the legend
        :return: None
        """

        trajs=self.get_trajectories_from_callsign_list(callsigns)
        num_traj=len(trajs)
        for ii in range(num_traj):
            latlon_data = trajs[ii].get_latlon_data()
            if color:
                plt.plot(latlon_data[:,1],latlon_data[:,0],color=color)
            else:
                plt.plot(latlon_data[:,1],latlon_data[:,0],label=callsigns[ii])
            plt.xlabel('lon(deg');plt.ylabel('lat(deg)')
        if legend:
            plt.legend()

    def read_xml_file(self,xml_file):
        """
        Given xml_file name, read AC trajectories into lists.
        xml.etree.ElementTree is used to parse the xml_file.

        Note:
        This must be called the instance to be non-empty

        :param xml_file: string name of xml file (output from NATS)
        :return: None (ACTrajectory instances are stored as internal variables)
        """
        fh=open(xml_file) #to close the file later
        tree=ET.parse(fh)
        root=tree.getroot()
        t_start_utc=int(root.get('simulation_start_time'))
        traj_list=root.findall('trajectory')
        print("will load {} ac trajectories...".format(len(traj_list)))
        #for the first aircraft

        for trajx in traj_list:
            #read the trajectory as an ATCTrajectory instance
            trajo=ACTrajectory(t_start_utc,trajx,'XML')
            #adding the trajectory
            #callsign=trajo.get_callsign()
            # self.callsign_list.append(trajo.get_callsign())
            # self.traj_list.append(trajo)
            self._add_trajectory(trajo)
            # print ("callsign:{} org_arpt:{}, dest_arpt:{}".format(
            #     callsign,trajx.get('origin_airport'),trajx.get('destination_airport')
            # ))
        print('done.')
        fh.close()

    def read_hdf5_file(self, h5_file):
        """
        Given h5_file name, read AC trajectories into lists

        Note:
        This must be called  for the instance to be non-empty

        :param h5_file: string name of hdf5 file (output from NATS)
        :return: None (ACTrajectory instances are generated as internal varialbes)
        """
        fh = h5py.File(h5_file)  # File instance
        #1.obtain dataset
        datset=fh['/trajectories']

        print("will load {} ac trajectories...".format(len(datset)))
        # for the first aircraft

        #later the h5 needs to include the following time.
        #Right now, it does not have the value.
        t_start_utc=1121238067

        for ii in range(len(datset)):
            # read the trajectory as an ATCTrajectory instance
            trajo = ACTrajectory(t_start_utc,datset[ii],'HDF5' )
            # adding the trajectory
            callsign = trajo.get_callsign()
            # self.callsign_list.append(trajo.get_callsign())
            # self.traj_list.append(trajo)
            self._add_trajectory(trajo)
            # print ("callsign:{} org_arpt:{}, dest_arpt:{}".format(
            #     callsign,trajx.get('origin_airport'),trajx.get('destination_airport')
            # ))
        print('done.')
        fh.close()


    def read_csv_file(self, csv_file):
        """
        Given csv_file name, read AC trajectories into lists

        Note:
        This must be called  for the instance to be non-empty

        :param csv_file: string name of the csv file (output from NATS)
        :return:
        """
        # 1. readout the header
        fh = open(csv_file, 'r')
        num_lines_discard = 7
        for ii in range(num_lines_discard):
            fh.readline()

        # a.read the start utc time
        line = fh.readline()
        tokens=line.rstrip().split(',')
        t_start_utc = int(tokens[0])

        #b. next line is empty line
        fh.readline()

        #c. starts to read 'AC' line
        ac_cursor=fh.tell()
        line=fh.readline()
        while line:

            #a. put the cursor back so that 'AC' line can be read
            fh.seek(ac_cursor)

            #b. file handle keeps moving the cursor inside
            trajo=ACTrajectory(t_start_utc,fh,type='CSV')
            self._add_trajectory(trajo)

            #c. read the next line
            line=fh.readline()
            #print("read line:{} len(line):{}".format(line,len(line)))

            #In both cases: (a) eof is reached (b) read line between AC trajectories
            if not line: #empty line (not '\n'), reached eof
                break
            else: #read the next line
                line=fh.readline() #does this cause an error if the file handler
                ac_cursor=fh.tell()
                #print(line)
        fh.close()


    def _add_trajectory(self,new_traj):
        """
        Since list is used to save trajectory, the name and the trajectory (call sign of aircraft are also
        saved)

        :param new_traj: ACTrajectory instance
        :return: None
        """
        self.callsign_list.append(new_traj.get_callsign())
        self.traj_list.append(new_traj)


class Region:
    """
    Both Center and Sector have the same format of data. So Region is introduced to handle the common
    attributes of Center and Sector.
    """

    def __init__(self,region_line):
        """
        read region specification from a read line. Both center and sector share
        the same format for their specification

        :param region_line: lines start with SECTOR or CENTER
        """

        tokens = region_line.rstrip().split(',')
        self.region_index=int(tokens[1])
        self.region_name=tokens[2]
        self.num_wpts=int(tokens[3])
        self.nwpts=None
        self.region_type=tokens[0]

    def get_retion_type(self):
        """
        whether center or sector
        :return: region type (string)
        """
        return self.region_type

    def get_region_name(self):
        """
        returns the name of the region (sector name or center name)

        :return: region_name (string)
        """
        return self.region_name

    def region_within_US(self):
        """
        checks whether the region belongs to the region around USA.
        This is to plot only those sectors and centers that are relevant US continent.

        :return:True or False
        """
        latlon_data=self.get_latlon_data()
        lat_min=np.min(latlon_data[:,0])
        lat_max=np.max(latlon_data[:,0])
        lon_min=np.min(latlon_data[:,1])
        lon_max=np.max(latlon_data[:,1])

        #the following are checked manually by looking at
        #google maps
        LAT_MIN_THLD=24
        LAT_MAX_THLD=68
        LON_MIN_THLD=-171
        LON_MAX_THLD=-54

        rtn_value=(lat_min > LAT_MIN_THLD) and \
                  (lat_max < LAT_MAX_THLD) and \
                  (lon_min > LON_MIN_THLD) and \
                  (lon_max < LON_MAX_THLD)

        return rtn_value

    def get_index(self):
        """
        returns the region index

        :return: region_index (sector or center index)
        """
        return self.region_index

    def get_number_of_waypoints(self):
        """
        tells the number of waypoints that compose the region (center or sector).
        The first and last are different, meaning that in plotting, the last and the first
        must be plotted to make a closed polygon.

        :return: number_of_waypoints (int)
        """
        return self.num_wpts

    def get_latlon_data(self):
        """
        Returns 2d array of (lat,lon)

        :return: numpy arrray of size (number_of_waypoints,2)
        """
        return self.nwpts

    def read_waypoints(self,fh):
        """
        This is a function that reads the given number of lines from a file
        The data seems to make angles between -180 and 180. To make a close region,
        when the longitude jumps by changing signs, subtract 360 degrees from them.

        :param fh: file_handle for SectorData or CenterData
        :return:
        """
        wpts = []
        num_lines = self.get_number_of_waypoints()
        for ii in range(num_lines):
            line = fh.readline()
            tokens = line.rstrip().split(',')
            lat = float(tokens[1])
            lon = float(tokens[2])
            if lon >-30:
                lon-=360

            wpts.append((lat, lon))

        self.num_wpts=len(wpts)
        self.nwpts=np.array(wpts) #numpy 2d array

    def plot_region(self,plt,color='w',fig_handle=None,centerId=False):
        """
        plot region (either sector or center)

        :return: None
        """
        #1.add the first point on the last again so that it can be closed
        latlon_data=self.get_latlon_data()
        lat_mean=np.mean(latlon_data[:,0])
        lon_mean=np.mean(latlon_data[:,1])
        first_latlon = latlon_data[0, :].reshape(1, 2)
        latlon_data = np.vstack((latlon_data, first_latlon))
        if len(latlon_data) > 1:
            plt.plot(latlon_data[:, 1], latlon_data[:, 0], '--', color=color, linewidth=.3)
            if centerId and fig_handle:
                #print("will add region id")
                ax0=fig_handle.get_axes()[0]
                cent_str='{}'.format(self.get_index())
                ax0.text(lon_mean,lat_mean,cent_str,color='green')
            plt.xlabel('lon(deg)');
            plt.ylabel('lat(deg)')

            plt.grid(linestyle=':', color='w', linewidth=0.3)

class Center(Region):
    """
    As of 01/12/2018, Region and Center are identical
    in terms of functions. They are only used for plotting.

    """
    def __init__(self,cent_line):
        Region.__init__(self,cent_line)



class Sector(Region):
    """
    Sector has specifications such as min and max altitudes.
    It inherits Region.
    """
    def __init__(self,sec_line):
        """
        read Sector specification from a read line

        :param sec_line: lines start with SECTOR
        """
        #print("sec_line:{}".format(sec_line))
        tokens = sec_line.rstrip().split(',')
        Region.__init__(self,sec_line)

        #besides, Sector also further specifies the following
        self.altmin_ft=float(tokens[4])
        self.altmax_ft=float(tokens[5])


    def get_sector_index(self):
        """
        return sector index

        :return: sector_index(integer)
        """
        return self.get_index()

    def get_max_altitude_ft(self):
        """

        :return: maximum altitude (ft)
        """
        return self.altmax_ft

    def get_min_altitude_tf(self):
        """

        :return: minimum altitude (ft)
        """
        return self.altmin_ft


class RegionHandler:
    """
    RegionHandler reads Sector or Center data files and store them as internal variables.
    The function 'plot_regions' displays the center or sector data.
    """
    def __init__(self):
        """
        do nothing
        """
        self.regions=None
        self.num_regions=None

    def getRegion(self,region_index):
        assert(len(self.regions)>0)
        return self.regions[region_index]

    def plot_regions(self,plt,color='m',fig_handle=None,regionId=False):
        """
        Plot stored region

        :param plt: matplotlib.pyplot instance
        :param color: specifies color of the line used for drawing regions
        :param fig_handle:
        :param regionId:
        :return:
        """

        for region in self.regions:
            region_name=region.get_region_name()
            # In case of center, there are high-centers and low centers with different boundaries.
            # Ignore high centers.
            if region_name.endswith('HIGH'):
                #print("region_name:{} will be discarded".format(region_name))
                continue
            if region.region_within_US():
                #print("displaying: {}".format(region_name))
                region.plot_region(plt,color,fig_handle,regionId)

    def read_region_file(self,region_file,region_type):
        """
        This function read a center or sector data file

        :param region_file: name of the data file
        :param region_type: string (used for differentiating sector and center)
        :return:
        """

        fh = open(region_file, 'r')
        # read 4 lines (heading)
        for ii in range(4):
            fh.readline()
        # starting from here reads sector data
        line = fh.readline()
        self.regions=[]
        while line: #Until it reads non-empty string
            if line.rstrip():  # if not empty line
                aregion=None
                if region_type=='SECTOR':
                    aregion=Sector(line)
                    aregion.read_waypoints(fh)
                elif region_type=='CENTER':
                    aregion=Center(line)
                    aregion.read_waypoints(fh)
                else:
                    raise ValueError("Right now only center and sector are considered")
                self.regions.append(aregion)

            line = fh.readline()  # read the next line
        self.num_regions = len(self.regions)
        print("total {} {}s are read".format(self.num_regions,region_type))
        fh.close()


class ACTrajectory:
    """
    ACTrajectory is introduced to handle numeric data read from NATS output.
    The following units are default:

    time:UTC miliseconds
    latitude:deg
    longitude:deg
    altitude: ft (altitude)
    altitude rate:fps  (rate of climb or descent)
    speed:knots (True AirSpeed)
    heading:deg
    fpa:deg (flight path angle)
    sector index: int

    For computational efficiency,  numpy array is used to denote all the dynamic variables
    except the static information regarding aircraft. The following maps define the numeric columns.

    colmap: provide column number for the variable name ex) t: time
            This provides the definition of columns when get_columns() is called.

    fm_map: defines flight_mode string and the integer number for the flight mode.

    n2imap: name to index map in order to read h5 extension.

    csv_header: description of column in csv file format.
    """
    colmap={'t':0,'lat':1,'lon':2,'alt':3,'speed':4,'heading':5,
            'altrate':6,'fpa':7,'sector_index':8,'flight_mode':9}

    fm_map={'DEPARTING':0,'CLIMB':1,'CRUISE':2,'DESCENT':3,'LANDING':4}

    n2imap = {'flight_index': 0, 'callsign': 1, 'actype': 2,
              'origin_airport': 3, 'destination_airport': 4,
              'start_time': 5, 'interval': 6,
              'latitude': 7, 'longitude': 8, 'altitude': 9,
              'hdot': 10, 'tas': 11, 'heading': 12,
              'fpa': 13, 'sector_index': 14, 'sector_name': 15,
              'mode': 16}

    csv_header={
        't':0, 'lat':1, 'lon':2,'alt':3,'hdot':4,'tas':5,'heading':6,
        'fpa':7,'sector_index':8,'sector_name':9,'flight_mode':10
    }

    def __init__(self,t0_utc,et_node_or_hdf5, type='HDF5'):
        """
       the second argument

        :param t0_utc: sim_start_time UTC (in miliseconds)
        """
        self.t0_utc=t0_utc
        self.flight_index = None
        self.callsign = None
        self.actype = None
        self.org_arpt = None
        self.dest_arpt = None
        self.start_time = None
        self.time_interval_milisec = None #for airborne
        self.nfields = None
        self.time_interval_milsec_ground=None #for ground

        if type=='XML':
            self.__initialize_from_xml(t0_utc,et_node_or_hdf5)
        elif type=='HDF5':
            self.__initialize_from_hdf5(t0_utc,et_node_or_hdf5)
        elif type=='CSV':
            file_handle=et_node_or_hdf5 #for CSV, it is a file handle
            self.__initialize_from_csv(t0_utc,file_handle)
        else:
            raise NameError("type must be either xml or hdf5")

    def __initialize_from_csv(self,t0_utc,fh):
        """

        :param t0_utc: UTC miliseconds for starting time
        :param fh: file_handle that starts reading 'AC'line
        :return:
        """
        #1. read AC line
        line=fh.readline()
        #print('read line:{}'.format(line))
        #2. read AC specification
        tokens=line.rstrip('\n').split(',')
        self.flight_index=int(tokens[1])
        self.callsign=tokens[2]
        self.actype=tokens[3]
        self.org_arpt=tokens[4]
        self.dest_arpt=tokens[5]
        t_start_sec=float(tokens[6])
        self.start_time = round(float(t_start_sec) * 1000) + t0_utc  # make miliseconds
        self.time_interval_milisec_ground=round(float(tokens[7])*1000)
        self.time_interval_milisec=round(float(tokens[8])*1000)

        num_rows=int(tokens[13])
        num_cols = 10
        self.nfields = np.zeros((num_rows, num_cols))
        for ii in range(num_rows):
            line=fh.readline()
            tokens=line.rstrip().split(',')
            #print("ii:{} line:{}".format(ii,line))
            delta_sec=float(tokens[self.csv_header['t']])
            self.nfields[ii, 0] = self.t0_utc + delta_sec * 1000
            self.nfields[ii,1]=float(tokens[self.csv_header['lat']]) #lat
            self.nfields[ii,2]=float(tokens[self.csv_header['lon']]) #lon
            self.nfields[ii,3]=float(tokens[self.csv_header['alt']]) #alt
            self.nfields[ii,4]=float(tokens[self.csv_header['tas']])
            self.nfields[ii,5] =float(tokens[self.csv_header['heading']])
            self.nfields[ii,6] =float(tokens[self.csv_header['hdot']])
            self.nfields[ii,7] =float(tokens[self.csv_header['fpa']])
            self.nfields[ii,8] =float(tokens[self.csv_header['sector_index']])
            #obtainint flight mode as a number
            flight_mode_str =tokens[self.csv_header['flight_mode']]
            flight_mode_num = ACTrajectory.fm_map[flight_mode_str]
            self.nfields[ii,9]=flight_mode_num

    def __initialize_from_hdf5(self, t0_utc, h5_traj):
        self.flight_index = h5_traj[self.n2imap['flight_index']]
        #print("flight index:{}".format(self.flight_index))

        self.callsign = h5_traj[self.n2imap['callsign']]
        self.actype = h5_traj[self.n2imap['actype']]
        self.org_arpt = h5_traj[self.n2imap['origin_airport']]
        self.dest_arpt = h5_traj[self.n2imap['destination_airport']]
        t_start_sec=h5_traj[self.n2imap['start_time']]
        self.start_time = round(float(t_start_sec) * 1000) + t0_utc  # make miliseconds

        self.time_interval_milisec = round(float(h5_traj[self.n2imap['interval']]) * 1000)
        #print("type:{},time_interval:{} miliseconds".format(type(self.time_interval_milisec),self.time_interval_milisec))

        #the number of rows
        num_rows=h5_traj[self.n2imap['latitude']].shape[0]
        num_cols=10;
        self.nfields = np.zeros((num_rows,num_cols))

        #a. fill up the time
        for ii in range(num_rows):
            self.nfields[ii,0]=self.start_time+ii*self.time_interval_milisec

        self.nfields[:,1]=h5_traj[self.n2imap['latitude']]
        self.nfields[:,2] = h5_traj[self.n2imap['longitude']]
        self.nfields[:,3] = h5_traj[self.n2imap['altitude']]
        self.nfields[:,4] = h5_traj[self.n2imap['tas']]
        self.nfields[:,5] = h5_traj[self.n2imap['heading']]
        self.nfields[:,6] = h5_traj[self.n2imap['hdot']]
        self.nfields[:,7] = h5_traj[self.n2imap['fpa']]
        self.nfields[:,8] = h5_traj[self.n2imap['sector_index']]
        self.nfields[:,9] = h5_traj[self.n2imap['mode']]


    def __initialize_from_xml(self,t0_utc,et_node):
        self.flight_index=int(et_node.get('flight_index'))
        self.callsign=et_node.get('callsign')
        self.actype=et_node.get('actype')
        self.org_arpt=et_node.get('origin_airport') #three chars
        self.dest_arpt=et_node.get('destination_airport')
        self.start_time=round(float(et_node.get('start_time'))*1000)+t0_utc #make miliseconds
        self.time_interval_milisec=round(float(et_node.get('interval'))*1000)
        #print("type:{},time_interval:{} miliseconds".format(type(self.time_interval_milisec),self.time_interval_milisec))

        self.nfields=[]

        traj_pts=et_node.findall('trajectory_point')
        for traj_pt in traj_pts:
            time=float(traj_pt.get('timestamp'))
            t_utc=ACTrajectory.compute_UTC_milis_time(self.start_time,time)
            lat=float(traj_pt.find('latitude_deg').text)
            lon=float(traj_pt.find('longitude_deg').text)
            alt=float(traj_pt.find('altitude_ft').text)
            alt_rate = float(traj_pt.find('rocd_fps').text)
            speed = float(traj_pt.find('tas_knots').text)
            heading = float(traj_pt.find('heading_deg').text)
            fpa = float(traj_pt.find('fpa_deg').text)
            secor_index = float(traj_pt.find('sector_index').text)
            flight_mode_str=(traj_pt.find('flight_mode').text)
            flight_mode_num=ACTrajectory.fm_map[flight_mode_str]
            #The following should match with the order of colmap
            self.nfields.append([t_utc,lat,lon,alt,speed,heading,alt_rate,fpa,secor_index,flight_mode_num])

        #make it numpy array for ease of handling later
        self.nfields=np.array(self.nfields)

    def get_callsign(self):
        """

        :return: return aircraft id (string)
        """
        return self.callsign

    def get_origin_airport(self):
        """

        :return: origin airport (string)
        """
        return self.org_arpt

    def get_destination_airport(self):
        """

        :return: desitnation airport (string)
        """
        return self.dest_arpt

    def get_all_times(self):
        """
        returns time columns in UTC miliseconds

        :return: numpy array of shape: (length,)
        """
        return self.nfields[:, self.colmap['t']]

    def get_initial_time(self):
        """
        return the very first time stamp of the aircraft trajectory

        :return:  integer in UTC miliseconds
        """
        return self.nfields[0,self.colmap['t']]

    def get_final_time(self):
        """
        returns the last time stamp of the aircraft trajectory

        :return: integer (for UTC miliseconds)
        """
        return self.nfields[-1,self.colmap['t']]

    def get_time_step_in_miliseconds(self):
        return self.time_interval_milisec

    def get_columns(self):
        """
        returns all the numeric data as numpy array. The defintion of columns
        are provided by the function call: get_column_definition()

        :return: ndarray (variables defined in column defintions)
        """
        return self.nfields

    def get_latlon_data(self):
        """
        returns lat_lon degree data

        :return: numpy.array((num_time_stamps,2))
        """
        lat_idx=self.colmap['lat']
        lon_idx=self.colmap['lon']

        lat=self.nfields[:,lat_idx:(lat_idx+1)] #make it 2d array
        lon=self.nfields[:,lon_idx:(lon_idx+1)]

        return np.hstack((lat,lon))

    def get_timed_latlon_data(self):
        """
        returns numpy array consisting of time_stamp,lat_deg,lon_deg

        :return: numpy array of numpy.array((num_time_stamp,3))
        """
        time_idx=self.colmap['t']
        lat_idx=self.colmap['lat']
        lon_idx=self.colmap['lon']
        time=self.nfields[:,time_idx:(time_idx+1)]
        lat=self.nfields[:,lat_idx:(lat_idx+1)] #make it 2d array
        lon=self.nfields[:,lon_idx:(lon_idx+1)]

        return np.hstack((time,np.hstack((lat,lon))))

    def get_latlon_at_given_time(self,time_msec):
        """
        Given time (in UTC miliseconds), return the [lat,lon] at the given time instance

        :param time_msec:  time stamp specified in UTC miliseconds
        :return: list of [lat,lon]
        """
        rtn_data=None
        all_times=self.get_all_times()
        time_indices=np.where(all_times==time_msec) #find indices for the given time
        if time_indices[0]: #if there is found one
            found_idx=time_indices[0][0] #because time_indices[0] is an array
            rtn_data=self._obtain_latlon_data_at_given_time_index(found_idx)
        return rtn_data

    def _obtain_latlon_data_at_given_time_index(self,data_index):
        """
        Given data_index, return [lat,lon]

        :param data_index: index for self.nfields
        :return: list: [lat,lon] at the given index
        """

        lat_idx = self.colmap['lat']
        lon_idx = self.colmap['lon']

        lat = self.nfields[data_index, lat_idx]  # make it 2d array
        lon = self.nfields[data_index, lon_idx]

        return [lat,lon]

    def plot_lat_lon(self,plt):
        """
        plot (lat,lon) in x-y plot

        :param plt: matplotlib.pyplot handle for plotting
        :return:
        """
        latlon_data=self.get_latlon_data()
        plt.plot(latlon_data[:,0],latlon_data[:,1])
        plt.xlabel('lat (deg)')
        plt.ylabel('lon(deg')

    @staticmethod
    def get_column_defintion():
        return ACTrajectory.colmap

    @staticmethod
    def compute_UTC_milis_time(t0_utc,delt_sec):
        """
        Compute the utc time in miliseconds

        :param t0_utc: init time in miliseconds integer
        :param delt_sec:  incremental time given in seconds
        :return: utc time in miliseconds
        """
        #comp_time=t0_utc+round(delt_sec*1000)
        #print("type(comp_time:{}".format(type(comp_time)))

        return t0_utc+round(delt_sec*1000) #int

class Node:
    """
    Node and Links are used to describe the surface layout of an airport.
    Node numbers are introduced to make ease the data access in a numerical form.
    """

    def __init__(self, node_num,node_name,lat_deg,lon_deg):

        self.node_num = node_num
        self.node_name=node_name
        self.lat_deg=lat_deg
        self.lon_deg=lon_deg
        self.rwy_entry=False
        self.rwy_name=None

    def get_node_name(self):
        """

        :return: node name (string)
        """
        return self.node_name

    def set_node_name(self,new_name):
        """
        set new_name as the node name.

        :param new_name:
        :return: None
        """
        self.node_name=new_name

    def get_node_num(self):
        """

        :return: node_number (int)
        """
        return self.node_num

    def set_node_num(self,node_num):
        """
        set node number.
        :param node_num: integer
        :return: None
        """
        self.node_num=node_num

    def get_lat_deg(self):
        """

        :return: latitude (degree)
        """
        return self.lat_deg

    def get_lon_deg(self):
        """

        :return: longitude (degree)
        """
        return self.lon_deg

    def get_latlon_deg(self):
        """

        :return: tuple of (lat_deg,lon_deg)
        """
        return (self.lat_deg,self.lon_deg)

    def get_runway_name(self):
        """
        This function must be called after the node is confirmed to be
        an runway entry
        :return:
        """
        assert(self.is_runway_entry())
        return self.rwy_name

    def is_runway_entry(self):
        """
        returns True if the node is a runway entry

        :return: True or False
        """
        return self.rwy_entry

    def set_runway_entry_flag(self,ibool):
        """
        set True or False on whether the the node is runway entry

        :param ibool: True or False
        :return: None
        """
        self.rwy_entry=ibool
    def set_runway_name(self,rwy_name):
        """
        set the runway name for the runway entry node

        :param rwy_name:
        :return:
        """
        self.rwy_name=rwy_name

class Link:
    """
    Link denotes a road segment that connects two nodes
    """

    def __init__(self, node1_num,node2_num):

        self.name = None
        self.linkid=(node1_num,node2_num) #tuple as a id
        self.start_node_num = node1_num
        self.end_node_num = node2_num
        self.length_ft = None  # initially negative (will be set by additonal process)

    def get_start_node_num(self):
        """

        :return: the node number for the start node
        """
        return self.start_node_num


    def get_end_node_num(self):
        """

        :return: the node number for the end node
        """
        return self.end_node_num


    def get_link_name(self):
        """
        link name convention: start_node_name-end_node_name

        :return: the link name
        """
        if self.name:
            return self.name
        else:
            raise ValueError("Link Name is not assigned yet.")

    def set_link_name(self,name):
        """
        set the given name as the link name

        :param name:
        :return: None
        """
        self.name=name

    def get_length_ft(self):
        """
        As of 04/02/2018, the length of link is not computed
        When the length of link is not computed, calling this function raises an error.

        :return: link length (float)
        """

        if self.length_ft:
            return self.length_ft
        else:
            raise ValueError("Link Length is not set.")

    # setters
    def set_length(self,new_length_ft):
        """
        set the length of the link

        :param new_length_ft:
        :return: None
        """
        self.length_ft = new_length_ft

class TaxiPlan:
    """
    For departure:[Gate, ...., Rwy,V2point]
    For arrival :[Touchdown,....,RwyExit,Gate]
    """



    def __init__(self,surf_layout):
        #empty
        self.arpt_layout=surf_layout
        self.wpts=[] #list of Node instance
        self.type=None
        #self.__read_type_str(type_str)

    def get_node_names(self):

        return [node.get_node_name() for node in self.wpts]

    def is_departure_plan(self):
        """
        if the taxiplan is for departure, it returns True.
        Else, it returns False.

        :return: True or False
        """
        return self.type=='dep'

    def get_runway_name(self):
        """
        Regardless of departure or arrival, the taxi plan involves the usage of runway.
        This function returns the runway used in the taxi plan.
        :return:
        """
        rwy_name=''
        #In the case of departure plan, the runway threshold point is the last or second last point
        #in the taxi plan.
        if self.is_departure_plan():

            rwy_node_name=self.get_departure_runway_node_name()
            rwy_name=self.arpt_layout.get_runway_name_from_node_name(rwy_node_name)
        else:
            #if the taxiplan is an arrival plan, the first point is an runway exit point.
            #From its name, the runway should be determined.
            rwy_exit_node_name=self.get_runway_exit_node_name()
            rwy_name=self.arpt_layout.get_runway_name_from_runway_exit_node_name(rwy_exit_node_name)

        return rwy_name

    def get_gate_node_name(self):
        """
        If the departure plan, the first point is viewed as the gate.
        For arrival, the last is viewed as the gate.

        :return:
        """

        #default is departure
        name=None
        if self.wpts:
            if self.type=='dep':
                name=self.wpts[0].get_node_name()
            if self.type=='arv':
                name=self.wpts[-1].get_node_name()
        return name

    def get_departure_runway_node_name(self):
        """
        The second last node is viwed as the departure runway (if V2 is included).
        Otherwise, the last point could be runway node for departure.

        :return: node_name that corresponds to the departure runway
        """
        if self.type=='arv':
            raise EnvironmentError(" this functio cannot be called for arrival taxi plan")
        else: #departure
            assert(len(self.wpts)>=2)
            #if the last is the runway entry, return it.
            if self.wpts[-1].is_runway_entry():
                return self.wpts[-1].get_node_name()
            else:
                return self.wpts[-2].get_node_name()

    def get_V2point_node_name(self):
        """
        For departure plan, the last one is the V2 point.

        :return:
        """

        if self.type=='arv':
            raise EnvironmentError(" this function cannot be called for arrival taxi plan")
        else:
            assert(len(self.wpts)>=3)
            #if the last point is the runway entry, there is no V2 point
            if self.wpts[-1].is_runway_entry():
                return None
            else: #otherwise, the last is V2 point
                return self.wpts[-1].get_node_name()

    def get_touchdown_node_name(self):
        """
        For arrival plan, the first one is the touchdown point.

        :return:
        """

        if self.type!='arv':
            raise EnvironmentError(" this function should be called for arrival taxi plan")
        else:
            # assert(len(self.wpts)>=3)
            # return self.wpts[0].get_node_name()
            #This may need to be revised later.
            return None

    def get_runway_exit_node_name(self):
        """
        For arrival plan, the seocnd one is the runway exit node.

        04/13/2018 Revision
        Arrival route design starts with selecting the runway exit.

        :return:
        """

        if self.type!='arv':
            raise EnvironmentError(" this function should be called for arrival taxi plan")
        else:
            assert(len(self.wpts)>=2)
            return self.wpts[0].get_node_name()

    def read_csv_route(self,csv_file):
        """
        When the user saves a designed route, it saves the route to a csv file
        in a specific way. This function reads the outputed csv file.

        :param csv_file: csv_filename for designed taxi route
        :return:
        """
        fr=open(csv_file,'r')
        #1.readingthe number of nodes
        fr.readline() #skip the first line
        line=fr.readline()
        tokens=line.rstrip('\n').split(',')
        num_points=int(tokens[1])
        #2.the next line is column description
        #node_number, node_name, lat_deg,lon_deg,alt_ft
        fr.readline()
        #3.Now read numeric data
        for ii in range(num_points):
            line=fr.readline()
            tokens = line.rstrip('\n').split(',')
            node_num = int(tokens[0])
            node_name = tokens[1]
            lat_deg = float(tokens[2])
            lon_deg = float(tokens[3])
            alt_ft=float(tokens[4])
            node_instance = Node(node_num, node_name, lat_deg, lon_deg)
            self.wpts.append(node_instance)

        #4. Final step:determin departure or arrival
        self.__set_taxiplan_type()

    def read_route_from_NATS_nodes(self, node_names):
        """
        The NATS returns list of node names (strings). This reads those strings
        into a sequence of Node instances.

        :param node_names: list of node names
        :return: None
        """

        print("Taxi Route from NATS")

        for node_name in node_names:

            node_instance=self.arpt_layout.get_node_from_name(node_name)
            self.wpts.append(node_instance)

        self.__set_taxiplan_type()

    def read_route_from_design_strings(self, display_strs):
        """
        In case of route design, the display string sometimes starts with 'RWxxxx' for runway
        entry points. So extract the node number from the designed string to get the corresponding
        Node instance.

        Logic: use the node_number to construct a route

        :param display_strs: "node_name(node_num)"
        :param surf_layout:
        :return:
        """

        print("Taxi route from design strings")


        for d_str in display_strs:
            #name_only=re.findall("([A-Za-z0-9_]+)\(",d_str)[0]
            node_num=re.findall("\(([0-9]+)\)",d_str)[0]
            node_instance=self.arpt_layout.get_node_from_node_number(int(node_num))
            #print("name_only:{}".format(name_only))
            self.wpts.append(node_instance)

        #determine taxiplan type
        self.__set_taxiplan_type()

    def plot_route(self,plt,label, linecolor=None):
        """
        plot the taxi route

        :param plt: matplotlib.pyplot
        :param label: for the case of legencs
        :param linecolor: if the user wants to specify the line color
        :return: None
        """
        #1.node
        lonlats=[(node.get_lon_deg(),node.get_lat_deg()) for node in self.wpts]
        lonlats=np.array(lonlats)
        if linecolor:
            plt.scatter(lonlats[:, 0], lonlats[:, 1], marker='o', c=linecolor, s=7)
            plt.plot(lonlats[:, 0], lonlats[:, 1], color=linecolor, label=label)
        elif label:
            plt.scatter(lonlats[:, 0], lonlats[:, 1], marker='o', c='y', s=7)
            plt.plot(lonlats[:, 0], lonlats[:, 1], '-y', label=label)


    def __set_taxiplan_type(self):
        """
        determine whether departure or arrival depending on
        the characteristics of the node-name sequence
        This must be called after the wpts are read

        :return: None
        """
        assert(len(self.wpts)>1) #at least three points
        start_node_name=self.wpts[0].get_node_name().upper()
        last_node_name=self.wpts[-1].get_node_name().upper()
        #if the first node is runway, it must be arrival
        if start_node_name.startswith('RW') or start_node_name.startswith('RWY'):
            self.type='arv'
        elif start_node_name.startswith('GATE'):
            self.type='dep'
        elif last_node_name.startswith('GATE'):
            self.type='arv'
        elif last_node_name.startswith('RW') or last_node_name.startswith('RWY'):
            self.type='dep'
        else:
            print("start_node:{}, end_node:{} are not sufficeint to determine type".format(\
                start_node_name,last_node_name))
            self.type='unknown'

    def write_taxi_route_lines_in_csv(self,fw):
        """

        :param fw: output file handle for csv output file
        :return:
        """

        fw.write("Number of points,{}\n".format(len(self.wpts)))
        fw.write("node_number, node_name, lat_deg,lon_deg, alt_ft\n")
        alt_ft=self.arpt_layout.get_altitude_ft()
        for node in self.wpts:
            node_num=node.get_node_num()
            node_name=node.get_node_name()
            if node.is_runway_entry():
                node_name=node.get_runway_name()
            lat = node.get_lat_deg()
            lon = node.get_lon_deg()
            fw.write("{},{},{},{},{}\n".format(node_num, node_name, lat, lon, alt_ft))


class AirportLayout:
    """
    Helper to process Airport Layout
    """
    def __init__(self,arpt_name):
        """
        In case of single file, it is XXXX_nodesNlinks.csv
        In case of two, node_xxx.csv and link_xxx.csv

        :param inode_file: node_xxx.csv
        :param ilink_file: link_xxx.csv
        """
        self.arpt_name=arpt_name
        self.alt_ft=-1000 #Airport Elevation
        self.nodes={} # dict: key:node_num value:Node instance
        self.node_map={} # (name to number map)
        self.links={} # dict, key as a tuple (node1_num,node2_num)
        self.node_rwy_map={} # key:node_num, value: runway_name

        #collection of links for all the runways for plotting
        #and future use
        self.rwy_nodes={}    # key:runway_name, value: list of node numbers on the runway

        #The followings are for storing and plotting user-defined routes when
        #the user selects a sequence of nodes for taxi-route design
        self.routes=[] #list of displayed node names for the user
        self.route_completed=False #made true when the user double clicks
        self.curr_node_str=None

        #when the user double clicks the route design, the shortest path is also
        #computed for comparison.
        self.design_plan=None #TaxiPlan instance
        self.default_plan=None #TaxiPlan instance

        #Line Drawing for user-selected points (this is for showing progress of node selections)
        self.xs=[]
        self.ys=[]
        self.line=None


    def initialize_from_NATS_airport_layout(self,nodemap,nodedata,linkdata,rwydata):
        """
        from NATS airport layout, build airport surface layout

        :param nodemap: obtained by calling airportInterface.getLayout_node_map(XXXX)
        :param nodedata: obtained by calling airportInterface.getLayout_node_data(XXXX)
        :param linkdata: obtained by calling airportInterface.getLayout_links(XXXX)
        :param rwydata : list of mapping between runway (CIFP) ident and node_name
        :return: None
        """
        num_nodes=len(nodemap)

        #self.nodes=[None for ii in range(num_nodes)]
        for ii in range(num_nodes):
            node_name=nodemap[ii][0]
            node_num=nodemap[ii][1].value
            assert(node_num==nodedata[ii][0].value)
            lat_deg=nodedata[ii][1].value
            lon_deg=nodedata[ii][2].value
            #if node_num==0 or node_num==1:
            #print("ii:{},node_name:{},node_num:{},lat:{},lon:{}".format(ii,node_name,node_num,lat_deg,lon_deg))
            node_instance = Node(node_num, node_name, lat_deg, lon_deg)
            self.nodes[node_num]=node_instance
            self.node_map[node_name]=node_num
            #print("check")
            #print(self.nodes[node_num].get_node_name())

        #2. read runway-node map
        for each_rwy in rwydata:
            rwy_name=each_rwy[0]
            node_name=each_rwy[1]
            node_num=self.node_map[node_name]
            #make the node to the runway entry
            self.nodes[node_num].set_runway_entry_flag(True)
            self.nodes[node_num].set_runway_name(rwy_name)
            #now runway name as a mapping for later purpose
            self.node_rwy_map[node_num]=rwy_name

        for key,value in self.node_rwy_map.items():
            print("node:{} {}".format(key,value))

        #3. links
        num_links = len(linkdata)
        for ii in range(num_links):
            node1_num = linkdata[ii][0].value
            node2_num = linkdata[ii][1].value
            # print("node1_num:{},node2_num:{}".format(node1_num,node2_num))
            # 1.create a link instance
            link_instance = Link(node1_num, node2_num)
            # 2.make a name
            node1_name = self.nodes[node1_num].get_node_name()
            node2_name = self.nodes[node2_num].get_node_name()
            link_name = node1_name + '-' + node2_name
            link_instance.set_link_name(link_name)
            # 3. add to the dictionary
            self.links[(node1_num, node2_num)] = link_instance

        #4. collect for each runway, what nodes are on the runway
        self.__assemble_paths_for_runways()


    def initialize_from_pickle(self,pickle_file):
        """
        initialize from pickle file for testing and development

        :param pickle_file: name of the pickle file
        :return:
        """

        fr = open(pickle_file,'r')
        arpt_data = pickle.load(fr)
        fr.close()

        self.node_map = arpt_data['nodemap']
        self.links = arpt_data['links']
        self.nodes = arpt_data['nodes']
        self.node_rwy_map = arpt_data['noderwymap']

        self.__assemble_paths_for_runways()

        for node_num, rwy_name in self.node_rwy_map.items():
            print("node_num:{}, node name:{}, rwy_name:{}".format(node_num,\
                self.nodes[node_num].get_node_name(),rwy_name))

    def initialize_from_two_csv_files(self,inodefile,ilinkfile):
        self.__reads_nodes_from_file(inodefile)
        self.__read_links_from_file(ilinkfile)
        self.__assemble_paths_for_runways()

        for rwy_name,rwy_nodes in self.rwy_nodes.items():
            print("rwy_name:{}, rwy_nodes:{}".format(rwy_name,rwy_nodes))


    def __reads_nodes_from_file(self, inode_file):
        """
        Given node_xxx.csv file, read nodes info

        :param inode_file:
        :return:
        """
        fr = open(inode_file, 'r')
        # 1.read header
        fr.readline()  # id,index,lat,lon,yEdId,domain,refName,type

        for line in fr:
            tokens = line.rstrip('\n').split(',')
            node_name = tokens[0]
            node_num = int(tokens[1])
            lat_deg = float(tokens[2])
            lon_deg = float(tokens[3])
            # print("node_name:{} node_num:{}, lat_deg:{} , lon_deg:{}".format(
            #     node_name,node_num,lat_deg,lon_deg
            # ))
            node_instance = Node(node_num, node_name, lat_deg, lon_deg)
            self.nodes[node_num] = node_instance
            self.node_map[node_name] = node_num
            #read refName for runway entry
            refName=tokens[6]
            if (refName.upper()!="NULL"):
                print("runway name:{}".format(refName))
                self.node_rwy_map[node_num]=refName #runway name
                node_instance.set_runway_entry_flag(True)
                node_instance.set_runway_name(refName)

        fr.close()

    def __read_links_from_file(self, ilink_file):
        """
        Given link_xxx.csv file, read links info

        :param ilink_file:
        :return:
        """
        fr = open(ilink_file, 'r')
        # 1.read header
        fr.readline()  # node1_name, node1_num,node1_lat,node1.lon,node2_name,node2_num,node2_lat,node2_lon

        for line in fr:
            if len(line.rstrip('\n'))>0:#for the case last line empty
                tokens = line.rstrip('\n').split(',')
                node1_num = int(tokens[1])
                node2_num = int(tokens[5])
                #print("node1_num:{}, node2_num:{}".format(node1_num,node2_num))
                # 1.create a link instance
                link_instance = Link(node1_num, node2_num)
                # 2.make a name
                node1_name = self.nodes[node1_num].get_node_name()
                node2_name = self.nodes[node2_num].get_node_name()
                link_name = node1_name + '-' + node2_name
                link_instance.set_link_name(link_name)
                # 3. add to the dictionary
                self.links[(node1_num, node2_num)] = link_instance
        fr.close()

    def get_airport_name(self):
        """
        ICAO airport name, for example: KPHX

        :return: ICAO airport name (string)
        """
        return self.arpt_name

    def get_altitude_ft(self):
        """

        :return: airport elevation in ft
        """
        if self.alt_ft <0:
            raise ValueError("Altitude for the airport not has been set yet")
        else:
            return self.alt_ft

    def set_altitude_ft(self,iAlt_ft):
        """
        set the altitude for the airport

        :param iAlt_ft: altifue_ft (float)
        :return:
        """
        self.alt_ft=iAlt_ft

    def get_designed_route(self):
        """
        returns the names of node names as displayed.

        :return: the list of node names (as displayed) to the user
        """
        return self.routes

    def get_designed_taxi_plan(self):
        """
        If there is a route designed (by mouse clicks), the sequence of node names are returned.
        The list of node names, displayed to the user and clicked by the user, is returned

        :return: list of node names (or CIFP runway names, for example, RW01L)
        """
        if self.design_plan:
            return self.design_plan
        else:
            print("No route is designed yet")
            return None

    def set_design_taxi_plan(self,aTaxiPlan):
        """
        This sets the design taxi plan.

        04/18/2018
        Currently, its main use is to make ease of printing out csv file of
        both design taxi plan and default taxi plan (shortest path algorithm)

        :param aTaxiPlan: TaxiPlan instance
        :return: None
        """
        self.design_plan=aTaxiPlan


    def get_default_taxi_plan(self):
        """
        If there is a route designed (by mouse clicks),the shortest path is also found
        for comparison.

        :return: TaxiPlan instance
        """

        if self.default_plan:
            return self.default_plan
        else:
            print("No default route yet")
            return None

    def set_default_taxi_plan(self,aTaxiPlan):
        """
        sets the default taxiplan as the given plan

        :param aTaxiPlan: TaxiPlan instance
        :return: None
        """
        self.default_plan=aTaxiPlan


    def get_node_from_node_number(self,node_num):
        """
        obtain Node instance using the node number

        :param node_num: (integer)
        :return: Node instance
        """
        if node_num in self.nodes.keys():
            return self.nodes[node_num]
        else:
            raise ValueError("Node number:{} not in keys".format(node_num))

    def get_node_from_name(self,node_name):
        """
        obtain Node instance with the given node name

        :param node_name: node name (string)
        :return: Node instance
        """

        if node_name in self.node_map.keys():
            return self.nodes[self.node_map[node_name]]
        else:
            raise NameError("Node_name:{} not recognized".format(node_name))

    def get_runway_name_from_node_name(self,node_name):
        """
        Given node_name, which corresponds to an runway entry point, the runway name
        is returned. This function must be called after the node name corresponds to
        the runway entry. When the given node name is not an runway entry, this call causes
        an error.

        :param node_name:
        :return: runway name (string) correponding to the node name
        """
        node_num=self.get_node_from_name(node_name).get_node_num()
        return self.node_rwy_map[node_num]


    def get_runway_name_from_runway_exit_node_name(self,rwy_exit_node_name):
        """
        Given runway exit node name, derive a runway name and returns it based on
        the following logics.
        1. obtain runway names that the given runway_exit_node can be located ex)RW01L RW19R
        2. out of two possible runways, select the farther one because this is a runway exit.

        :param rwy_exit_node_name: string
        :return: runway_name (string)
        """
        rwy_exit_node=self.get_node_from_name(rwy_exit_node_name)
        rwy_exit_node_num=rwy_exit_node.get_node_num()

        #1. Find any runway to which the runway exit node belongs
        possible_rwy_entry_nodes=None
        for rwy_name,nodes_in_the_rwy in self.rwy_nodes.items():
            if rwy_exit_node_num in nodes_in_the_rwy:
                possible_rwy_entry_nodes=(nodes_in_the_rwy[0],nodes_in_the_rwy[-1])

        print(" Runway entry can either be {}".format(possible_rwy_entry_nodes))

        #2.obtain the farther one
        rwy_node_num=self.get_farther_one_out_of_two(rwy_exit_node_num,possible_rwy_entry_nodes[0],
                                                     possible_rwy_entry_nodes[1])

        print("Runway name:{}".format(self.node_rwy_map[rwy_node_num]))

        #3.returns it
        return self.node_rwy_map[rwy_node_num]


    def get_farther_one_out_of_two(self,current_node_num,node1_num,node2_num):
        """
        Given two node numbers, return the farther one out of two from the current node_num

        :param current_node_num:
        :param node1_num:
        :param node2_num:
        :return: node_num that corresponds to the farther node (out of two nodes)
        """
        current_node=self.get_node_from_node_number(current_node_num)
        node1=self.get_node_from_node_number(node1_num)
        node2=self.get_node_from_node_number(node2_num)

        #In the surface, Eucledian is sufficient for finding out the closer one
        dist1=self.obtain_Eucledian_distance_between_two_latlons(current_node.get_latlon_deg(),
                                                                 node1.get_latlon_deg())
        dist2=self.obtain_Eucledian_distance_between_two_latlons(current_node.get_latlon_deg(),
                                                                 node2.get_latlon_deg())
        rtn_node_num=node2_num
        if dist1> dist2:
            rtn_node_num=node1_num

        return rtn_node_num


    def obtain_Eucledian_distance_between_two_latlons(self,latlon1, latlon2):
        """
        Technically speacking, the distance between two latlons should be obtained
        using formulas that computes the grand line distance. For the airport surface,
        the Earth curvature can be ignored, and (lat,lon) is treated as if x-y.
        This computes the Eucledan distance between two lat-lon points.
        :param latlon1 tuple
        :param latlon2 tuple
        :return: Eucledean distance betweewn two latlon points
        """

        return np.sqrt((latlon1[0]-latlon2[0])**2+(latlon1[1]-latlon2[1])**2)


    def get_nodes(self):
        """
        returns all the nodes in the airport layout

        :return: nodes (dictionary with node numbers as keys)
        """
        return self.nodes

    def get_links(self):
        """
        obtain all the links
        :return: dict with keys as the tuple (node1_num,node2_num) corresponding to the start and end node numbers
        """
        return self.links

    def get_runway_node_numbers(self):
        """
        returns node numbers for runway threshold nodes
        :return:
        """
        return list(self.node_rwy_map.keys())

    def get_route_completion_flag(self):
        """
        tells whether the route design is finished.
        The route_completion_flag is set to True when the user double clicks the last node.

        :return: True or False whether the route design is finished
        """
        return self.route_completed

    def set_route_completion_flag(self,ibool):
        """
        marks that the roude design is completed

        :return: None
        """
        self.route_completed=ibool

    def have_a_designed_route(self):
        """
        tells True whether the airport layout has a non-empty node-name sequence and
        the route design is completed. In other words, the airport surface has a designed route
        only if the route is non-empty and the user double-clicked the last node.

        :return: True or False
        """

        #If the routes are not None and they are completed
        if self.routes and self.get_route_completion_flag():
            return True
        else:
            return False


    def plot_airport_layout(self,plt):
        """
        Plot nodes and links in (lon,lat) coordinates
        In this plot, even if the user designs a taxi route, it will not be compared to
        the one of the shortest path

        :param plt: handle for matplotlib.pyplot
        :return: None
        """
        self.plot_nodes_lonlat(plt)
        self.plot_links_lonlat(plt)

    def plot_airport_layout_connectivity(self,plt,convity):
        self.plot_nodes_lonlat(plt)
        self.plot_links_lonlat(plt,iConnectivity=convity)



    def plot_airport_for_taxiroute_design(self,plt,airportInterface,ac_instance):
        """
        Plot nodes and links in (lon,lat) coordinates
        As of 04/02/2018, Aircraft Instance is mainly used for obtaining aircraft id (call sign).

        :param plt: matplotlib.pyplot handle
        :param airportInterface: NATS airportInterface to call shortest-path-route function
        :param ac_instance: NATS Aircraft Instance for obtaining the information about the aircraft
        :return: None
        """


        self.plot_nodes_lonlat(plt,airportInterface,ac_instance)
        self.plot_links_lonlat(plt)


    def plot_default_taxiplan(self,plt,airportInterface,ac_instance):
        """
         Plot the default taxiplan corresponding to the designed plan
         When the user designs a taxi plan, a default taxi plan, designed using the shortest path algorithm,
         is displayed together. The default taxi plan is obtained using (gate_name,dep_rwy,V2 point) in departure
         and (touchdown point, runway exit, gate name) in arrival.

         Revision:04/13/2018

         When the user double clicks at the departure runway, the departure plan ends at the runway threshold.
         This type of interaction is also allowed.

        :param plt: matplotlib.pyplot handle
        :param airportInterface: NATS airportInterface instance
        :param ac_instance:  NATS Aircraft Instance
        :return: None
        """

        if self.have_a_designed_route():
            designed_taxi_route = self.get_designed_route()
            print("designed_plan:{}".format(designed_taxi_route))
            design_plan = TaxiPlan(self)
            design_plan.read_route_from_design_strings(designed_taxi_route)
            self.set_design_taxi_plan(design_plan)

            #depending on arrival or departure, designed_taxi_route is used differently
            default_plan_str=None
            if design_plan.is_departure_plan():
                default_plan_str=self.__obtain_default_deparrture_node_name_sequence(design_plan,\
                                                                                     airportInterface,\
                                                                                     ac_instance)
            else: #arrival plan
                default_plan_str = self.__obtain_default_arrival_node_name_sequence(design_plan, \
                                                                                       airportInterface, \
                                                                                       ac_instance)


            #TaxiPlan instance for default route
            default_plan = TaxiPlan(self)
            default_plan.read_route_from_NATS_nodes(default_plan_str)
            #for the case of saving default routes as well
            self.set_default_taxi_plan(default_plan)

            #plot
            design_plan.plot_route(plt, label='designed', linecolor='b')
            default_plan.plot_route(plt, label='shortest_algorithm', linecolor='r')
            plt.legend()

    def plot_nodes_lonlat(self, plt,airportInterface=None,ac_instance=None,line_style='om'):
        """
        plot links in (lon_deg,lat_deg) format. This plot hanldes all the user interaction with
        the figure in designing a taxi plan. Look at the code for details.

        :param plt: matplotlib.pyplot
        :param line_style:
        :return: None
        """
        lonlats=np.zeros((len(self.nodes),2))
        for ii in range(len(self.nodes)):
            lonlats[ii,0]=self.nodes[ii].get_lon_deg()
            lonlats[ii,1]=self.nodes[ii].get_lat_deg()

        #1.Nodes are displayed using the scattered plots.
        # c: color s: size (in points)
        sc=plt.scatter(lonlats[:,0], lonlats[:,1],marker='o',c='xkcd:teal',s=7)
        #2. the scatter plot will be annotated with the airport name
        lon_avg=np.mean(lonlats[:,0]);lat_max=np.max(lonlats[:,1])
        plt.annotate(self.get_airport_name(),xy=(lon_avg,lat_max),color='xkcd:teal')

        #3. The following annotation is to display node name (number) when the mouse on the node
        annot = plt.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                             bbox=dict(boxstyle="round", fc="w"),
                             arrowprops=dict(facecolor='r',arrowstyle="->"))
        annot.set_visible(False)

        #4.getting fig,ax for later use
        fig=plt.gcf()
        ax=plt.gca()

        #5. The curr_node_str is recorded for it to update annotation and route design
        # the mouse click control is used, once the mouse is double clicked, the mouse click does not
        # append the node for taxiway route anymore.

        self.curr_node_str=None
        self.mouse_click_cid=None


        def update_annot(attr_dict):
            """
            The position of the annotation is gotten from mouse_location_event attributes.
            node name is obtained from the node_number information (scatter dot number)
            And text is formed such that node_name(node_number).

            :param attr_dict: attributes of mouse motion event
            :return: annotation_text which will be didplayed in a specified offset position to
                     the annotation position
            """
            node_num=attr_dict["ind"][0]
            pos = sc.get_offsets()[node_num]
            annot.xy = pos
            #print("attr[ind]:{}".format(attr_dict["ind"]))

            node_name=self.nodes[node_num].get_node_name()
            text = "{}({})".format(node_name,str(node_num))
            if self.nodes[node_num].is_runway_entry(): #if runway
                text="{}({})".format(self.node_rwy_map[node_num],str(node_num))

            #whenever the mouse is on the node, update the current node
            annot.set_text(text)
            annot.get_bbox_patch().set_facecolor('y')
            annot.get_bbox_patch().set_alpha(0.6)
            return text

        def hover(event):
            """
            When mouse event is contained in the scatter plot, the following happens.
            a. node string is update by calling the function: update_annot to retrieve
            the node name and number information that the mouse is over
            b.the annotation is made visible.

            :param event: (mouseevent)
            :return: None figure is redrawn
            """
            vis = annot.get_visible()
            if event.inaxes == plt.gca():
                cont, attr_dict = sc.contains(event)
                if cont:
                    self.curr_node_str=update_annot(attr_dict)
                    #print("curr_node_str:{}".format(self.curr_node_str))
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        fig.canvas.draw_idle()

        def on_press(event):
            """
            This function is called when the mouse button is pressed.
            1. When the mouse is pressed upon the node, the node name is appended to
            the list of self.route. The line data (self.xs,self.ys) are updated as the positio of the mouse
            and drawn. However, for the route, the node on display is collected.
            2. when the mouse is double-clicked

            :param event:
            :return:
            """

            if event.inaxes!=ax: return
            #a. only handles the mouse is clicked on the scattered nodes
            vis=annot.get_visible()
            if vis: # and the node name is being displayed
                if event.dblclick:
                    #print("event.dblclick:{}".format(event.dblclick))
                    print("{} will be added to the route.".format(self.curr_node_str))
                    print("the mouse click will not be accepted anymore")
                    fig.canvas.mpl_disconnect(self.mouse_click_cid)
                    print("TaxiRoute:{}".format(self.routes))
                    self.set_route_completion_flag(True)

                    #when the user double clicks, a default taxi-route based on the shortest path
                    #algorithm is also displayed.
                    if airportInterface: #if there is an airportInstance, then draw default plot
                        time.sleep(2)
                        self.plot_default_taxiplan(plt,airportInterface,ac_instance)
                else: #single click
                    print("{} will be added to the route.".format(self.curr_node_str))
                    #1. save the current node string
                    self.routes.append(self.curr_node_str)
                    #2. update the route lines
                    self.xs.append(event.xdata);self.ys.append(event.ydata)
                    self.line.set_data(self.xs,self.ys)
                    self.line.figure.canvas.draw()


        #6. The following sets lines and make connections between canvas and the the mouse
        self.line, = ax.plot([], [], '-b')  # empty line
        fig.canvas.mpl_connect("motion_notify_event", hover)
        self.mouse_click_cid=fig.canvas.mpl_connect("button_press_event",on_press)


    def plot_links_lonlat(self, plt, line_style='-', iConnectivity=None):
        """
        plot links in (lon_deg,lat_deg) format

        :param plt: matplotlib.pyplot
        :param line_style:
        :return: None
        """

        #1. Assemble all the nodes that are on runways
        all_rwy_node_nums=[]
        for key, rwy_nodes in self.rwy_nodes.items():
            #print("Rwy:{} nodes:{}".format(key,rwy_nodes))
            for node_num in rwy_nodes:
                if node_num not in all_rwy_node_nums:
                    all_rwy_node_nums.append(node_num)

        #2. Plot links using different colors for runways and taxi,ramp ways
        for lkey, link in self.links.items():
            node1_num = lkey[0]
            node2_num = lkey[1]

            lat1, lon1 = self.nodes[node1_num].get_latlon_deg()
            lat2, lon2 = self.nodes[node2_num].get_latlon_deg()

            lons = [lon1, lon2]
            lats = [lat1, lat2]


            #check if it is a runway segment
            taxi_line_width=0.5
            rwy_line_width=3


            #the following is for checking connectivity
            if iConnectivity is not None: #if connectivity is no None
                #check if the link is blocked
                if iConnectivity[node1_num][node2_num]==0: #connected
                    plt.plot(lons,lats,line_style,color='r')
                else:
                    plt.plot(lons,lats,line_style,color='xkcd:teal',linewidth=taxi_line_width)
            else:
                # if both node1 and node2 are on runways,the link is displayed using different
                # color and style
                if node1_num in all_rwy_node_nums and node2_num in all_rwy_node_nums:
                    # if lkey in rwy_lkeys:
                    plt.plot(lons, lats, '-', color='xkcd:grey', linewidth=rwy_line_width)
                else:

                    plt.plot(lons, lats, line_style, color='xkcd:teal', linewidth=taxi_line_width)  # plot(lon,lat)

        #add grid
        plt.grid(color='black')

    def write_taxiRoute_to_csv(self,out_filename):
        """
        write the designed route to a taxi route in csv format

        :param out_filename
        :return: None
        """
                #2. out_filename
        fw=None
        design_plan=self.get_designed_taxi_plan()
        if design_plan:
            fw=open(out_filename,'w')
            fw.write(("User selected Routes\n"))
            design_plan.write_taxi_route_lines_in_csv(fw)

        default_plan=self.get_default_taxi_plan()
        if default_plan:
            print("default route will be written..")
            fw.write("\n") #add a line
            fw.write("Shortest Path Routes\n")
            default_plan.write_taxi_route_lines_in_csv(fw)

        if fw:
            fw.close()
            print("{} has been written.".format(out_filename))

    def __write_taxiRoute_lines(self, fw,node_names):

        fw.write("Number of points,{}\n".format(len(node_names)))
        fw.write("node_number, node_name, lat_deg,lon_deg, alt_ft\n")
        alt_ft=self.get_altitude_ft()
        for node_str in node_names:
            node_name = re.findall("([A-Za-z0-9_]+)", node_str)[0]
            node_num_str = re.findall("\(([0-9]+)\)", node_str)[0]
            node_num = int(node_num_str)
            lat = self.nodes[node_num].get_lat_deg()
            lon = self.nodes[node_num].get_lon_deg()
            fw.write("{},{},{},{},{}\n".format(node_num, node_name, lat, lon, alt_ft))


    def write_airport_data_to_pickle(self,out_filename):
        """
        Write the airport data to a given filename for testing

        :param out_filename: xxxxx.pckl
        :return: None
        """
        arpt_data = {}
        arpt_data['nodemap'] = self.node_map
        arpt_data['nodes'] = self.nodes
        arpt_data['links'] = self.links
        arpt_data['noderwymap'] =self.node_rwy_map

        fw=open(out_filename,'wb')
        pickle.dump(arpt_data,fw)
        fw.close()
        print("airport layout has been written to {}".format(out_filename))


    def write_airport_layout_to_kml(self,outdir=None):
        """
        Writhe a kml file to the user-specified filename. The resulting kml file can
        be loaded to Google My Maps for display

        :param out_filename: output filename ending with '.kml'
        :return: None. Output file name of "AirportLayout_xxxx.kml" will be generated with xxxx denoting airport id.
        """
        #1. header specifying markers for nodes and links
        header = self.__get_kml_style()
        #2.output filename
        kml_outfile="AirportLayout_"+self.get_airport_name()+'.kml'
        if outdir:
        	kml_outfile=os.path.join(outdir,kml_outfile)
        fw = open(kml_outfile, 'w')
        fw.write(header)
        #3. Folder contains specific data for airport layout
        fw.write("\n<Folder>\n")
        fw.write("<name>" + self.get_airport_name()+ "</name>\n")
        fw.write("<open>1</open>\n")
        # a.write node first
        for node_name,node in self.nodes.items():
            pl_str = self.__obtain_node_placemark_str(node)
            fw.write(pl_str)
        # b.write link
        for link_key, link in self.links.items():
            pl_str = self.__obtain_link_placemark_str(link)
            fw.write(pl_str)
        #4.match the closing tags
        fw.write("</Folder>\n" + "</Document>\n" + "</kml>")
        fw.close()
        print("{} has been written.".format(kml_outfile))

    def __obtain_default_deparrture_node_name_sequence(self,design_plan_obj,airportInterface,ac_instance):
        """
        This function must be called after design_plan_obj is the TaxiPlan instance with departure confirmation

        :param design_plan_obj:
        :param airportInterface:
        :param ac_instance:
        :return: None
        """

        gate_name = design_plan_obj.get_gate_node_name()
        #The following only works for deaprture plan
        rwy_node_name = design_plan_obj.get_departure_runway_node_name()
        V2_node_name = design_plan_obj.get_V2point_node_name()

        print("Gate:{} rwy:{} V2:{}".format(gate_name,rwy_node_name,V2_node_name))

        # Shortest Path design from the designed route
        ac_id=ac_instance.getAcid()

        arpt_name = airportInterface.getDepartureAirport(ac_id)

        # This will be replaced later if NATS is ready.
        #sp_plans_jStr = airportInterface.generate_taxi_route_from_A_To_B(ac_instance.getAcid(), arpt_name, gate_name, \
        #                                                                 rwy_node_name)
        if V2_node_name: #if there is a V2 point
            airportInterface.generate_surface_taxi_plan(ac_id,arpt_name,gate_name,rwy_node_name,V2_node_name,None)
        else:
            #the end is runway node name, in this case, obtain runway name using the rwy_node_name
            rwy_name=self.get_runway_name_from_node_name(rwy_node_name)
            airportInterface.generate_surface_taxi_plan(ac_id,arpt_name,gate_name,rwy_node_name,rwy_name)

        java_plan_strs = airportInterface.getSurface_taxi_plan(ac_id, arpt_name)
        default_plan_strs=[]
        for ii in range(len(java_plan_strs)):
            default_plan_strs.append(java_plan_strs[ii])


        # sp_plans = []
        # for ii in range(len(sp_plans_jStr)):
        #     sp_plans.append(str(sp_plans_jStr[ii]))
        #
        # sp_plans.append(V2_node_name)
        print("default_departure_plan:{}".format(default_plan_strs))

        return default_plan_strs

    def __obtain_default_arrival_node_name_sequence(self, design_plan_obj, airportInterface, ac_instance):
        """
        This function must be called after design_plan_obj is the TaxiPlan instance with arrival confirmation

        :param design_plan_obj:
        :param airportInterface:
        :param ac_instance:
        :return:
        """

        gate_name = design_plan_obj.get_gate_node_name()
        # The following only works for deaprture plan
        rwy_exit_name = design_plan_obj.get_runway_exit_node_name()
        td_node_name = design_plan_obj.get_touchdown_node_name()

        print("Gate:{} rwy_exit:{} touchdown:{}".format(gate_name, rwy_exit_name, td_node_name))

        # Shortest Path design from the designed route
        ac_id = ac_instance.getAcid()
        arpt_name = airportInterface.getArrivalAirport(ac_id)

        # (ac_id,ariprot_code,startNode,endNode,V2node_latlon,touchdown node_latlon)
        #td_node_obj = self.get_node_from_name(td_node_name)
        #td_lat_lon = [td_node_obj.get_lat_deg(), td_node_obj.get_lon_deg()]
        if td_node_name:
            airportInterface.generate_surface_taxi_plan(ac_id, arpt_name, rwy_exit_name, gate_name, None, td_node_name)
        else: #without touchdown point
            rwy_name=design_plan_obj.get_runway_name()
            airportInterface.generate_surface_taxi_plan(ac_id,arpt_name,rwy_exit_name,gate_name,rwy_name)
            #need to know runway name?


        java_plan_strs = airportInterface.getSurface_taxi_plan(ac_id, arpt_name)
        # sp_plans = []
        # for ii in range(len(sp_plans_jStr)):
        #     sp_plans.append(str(sp_plans_jStr[ii]))
        #
        # sp_plans.append(V2_node_name)
        default_plan_strs = []
        for ii in range(len(java_plan_strs)):
            default_plan_strs.append(java_plan_strs[ii])

        #default_plan_strs.insert(0,td_node_name)
        print("default_arrival_plan:{}".format(default_plan_strs))

        return default_plan_strs

    def __assemble_paths_for_runways(self):
        """
        Given node_runway_map that provides runway_node to runway_name, collect the intermediate
        nodes for each runway designation. Later, these nodes can be used for denoting nodes and links
        on each runway.

        :return: None
        """
        #print("inside _assemble_paths_for_runways")
        for rwy_node_num, rwy_name in self.node_rwy_map.items():
            node_name = self.nodes[rwy_node_num].get_node_name()
            print("node_num:{} rwy_name:{},node_name:{}".format(rwy_node_num, rwy_name, node_name))
            rwy_str_to_match = self.__obtain_possible_runway_names(node_name)[0]

            print("Rwy_str_to_match: {}".format(rwy_str_to_match))
            self.rwy_nodes[rwy_name] = self.__assemble_nodes_on_the_runway([rwy_node_num], rwy_str_to_match)


    def __assemble_nodes_on_the_runway(self, current_route, rwy_str_to_match):
        """
        The recursive algorithm works as follows.
        1. check if current_routes is empy, if so, it means the node assembly up to another runway
           is not possible with the current routes
        2. check if the current_routes is complete with the last as an entry point, then done.
        2. If not, for the last node, obtain possible nodes that are on the runway.
        3. For each possible nodes, obtain the the routes by calling calling the assemble_nodes_on_the_runway
           with extended routes.

        Technically speaking, each node at least and at most, one list of nodes that connect to another runway
        for example RW01L-RW19R.

        :param current_route: list of node_numbers up to this point
        :param rwy_str_to_match: ex) Rwy_01, when another node is added
        :return: current route or augmented route (depending on the recursion stage)
        """

        # 1. Final condition condition
        rtn_route = []
        # 1.a Final condition A. the current routes are empty

        if current_route:
            print("current_route:{}".format(current_route))
            last_node_num = current_route[-1]
            # 1.b Final Condition B: the current routes are complete (reached another runway)
            if len(current_route) > 1 and self.nodes[last_node_num].is_runway_entry():

                rtn_route = current_route  # the current route is complete
                start_rwy_name = self.node_rwy_map[current_route[0]]
                end_rwy_name = self.node_rwy_map[current_route[-1]]
                print("found complete routes:{}-{}".format(start_rwy_name, end_rwy_name))
            # 2. The current routes are neither empty or complete.
            else:
                # 2.a.find all the runway nodes that are connected with the last node (not previsouly trodden)
                next_nodes = self.__find_next_nodes_on_the_runway(current_route[:-1], last_node_num, rwy_str_to_match)
                if next_nodes:  # if there are next_nodes

                    # 2.b for each another node on the runway, extend the current routes, and assemble the routes
                    # with the updated routes
                    for each_node in next_nodes:
                        updated_curr_route = copy.deepcopy(current_route)
                        updated_curr_route.append(each_node)
                        candidate_route = self.__assemble_nodes_on_the_runway(updated_curr_route, rwy_str_to_match)
                        # 3. If there is a route that can be assembled, return it. Because of the runway characteristic
                        # canndiate_route can at most be single one. Otherwise, its empty.
                        if candidate_route:
                            rtn_route = candidate_route
        return rtn_route

    def __find_next_nodes_on_the_runway(self, prev_rwy_routes, c_node_num, rwy_str_to_match):
        """
        out of all the links that are connected to the last node, remove those that are already trodden
        Find and returns nodes that can be extended from the current node number.

        :param prev_rwy_routes: list of node_numbers that are already trodden (the currently progressing route)
        :param c_node_num:  the current node number (int)
        :param rwy_str_to_match: runway string to match ex) Rwy_01
        :return: list of node numbers that can be extended from the current node, in case of runway, it is at most one.
        """

        # step 1. find all the links that are connected with the current node
        link_keys_conncecting_c_node = []
        for link_key in self.links.keys():
            if link_key[0] == c_node_num or link_key[1] == c_node_num:
                link_keys_conncecting_c_node.append(link_key)

        # print("connecting links:{}".format(link_keys_conncecting_c_node))

        # step 2. out of connecting links, find the ones that are on the same runway but are not visited previously
        # Technically speaking, such a node is at most one.

        rtn_nodes = []
        for link_key in link_keys_conncecting_c_node:
            another_node_number = self.__obtain_another_node_number(c_node_num, link_key)
            if not (another_node_number in prev_rwy_routes):
                # print("another_node {} is a candidate for runway check".format(another_node_number))
                if self.__another_node_number_can_be_on_the_same_runway(another_node_number, rwy_str_to_match):
                    rtn_nodes.append(another_node_number)

        return rtn_nodes

    def __another_node_number_can_be_on_the_same_runway(self, another_node_number, rwy_str_to_match):
        """
        checks whether the given node number can be on the runway specified by runway string to match ex) Rwy_01

        :param another_node_number: node_number that needs to be check (int)
        :param rwy_str_to_match:   runway string that must be matched (string)
        :return:  True or False
        """

        rtn_value = False

        another_node_name = self.nodes[another_node_number].get_node_name()
        another_node_possible_rwy_names = self.__obtain_possible_runway_names(another_node_name)

        # print("another_node_possible_rwy_names:{}".format(another_node_possible_rwy_names))
        if another_node_possible_rwy_names:  # if there are possible runway names

            # print("another_node_possible_rwy_names:{}".format(another_node_possible_rwy_names))
            rtn_value = self.__another_node_name_can_be_on_the_same_runway(rwy_str_to_match,
                                                                           another_node_possible_rwy_names)

        return rtn_value

    @staticmethod
    def __obtain_another_node_number(given_node_num, iLink_key):
        """
        Given node_number and a single link, return the node number which is not given node number

        :param given_node_num: int: node_number to compare
        :param iLink_key:  int: link that contains the node number
        :return: int: node number of the link that is not given node number
        """
        rtn_num = iLink_key[0]
        if rtn_num == given_node_num:
            rtn_num = iLink_key[1]
        return rtn_num

    def __another_node_name_can_be_on_the_same_runway(self, rwy_str_to_match, anode_possible_rwy_names):
        """
        compare possible runway combinations and determine if the second node could be on the same runway
        For normal runway node, such as Rwy_01_004, the runway string to match can be directly obtained.
        However, for runway crossing node, Rwy_01_04, the node can be on both Rwy_01 or Rwy_04. This function
        checks the given possible rwy names for another node contain the runway match string.

        :param runway_to_match: runway string, ex) Rwy_01
        :param node2_possible_rwy_names: list of string
        :return:True or False
        """
        rtn_value = False
        if anode_possible_rwy_names:  # there is a possible runway name
            # and matches with the runway_match_string
            rtn_value = (rwy_str_to_match in anode_possible_rwy_names)

        return rtn_value

    @staticmethod
    def __obtain_possible_runway_names(node_name):
        """
        Given node name, returns the list of runway strings that can be extracted from the node name.
        For example, node_names of Rwy_01_003, Rwy_01_04 (for rwy crossing node), Txy_A_007
        lead to [Rwy_01],[Rwy_01,Rwy_04], and [].

        :param node_name: node_name
        :return: list of runway strings that can be extracted from given name  ex) [Rwy_01] or [Rwy_01,Rwy_04]
        """
        rtn_list = []
        if node_name.startswith('Rwy'):  # Node must start with Rwy

            tokens = node_name.split('_')
            # 1.primary runway string
            rwy_str = tokens[0] + '_' + tokens[1]

            # 2. In case of runway crossing nodes, the last have two digits
            # and another runway string can be formed.
            rwy_str_alt = None
            if len(tokens[2]) == 2:  # indicates runway crossing point
                rwy_str_alt = tokens[0] + '_' + tokens[2]

            # If there is another runway string,
            # make two runway strings otherwise make one.
            if rwy_str_alt:  # if the node is runway crossing point
                rtn_list = [rwy_str, rwy_str_alt]
                # print("rwy_str: {} rwy_str_alt: {}".format(rwy_str, rwy_str_alt))
            else:
                rtn_list = [rwy_str]

        return rtn_list


    def __obtain_node_placemark_str(self,node):
        """
        Given node,builds and returns a placemark string for a node

        :param node: Node instance
        :return: a string of <Placemark>...</Placemark>
        """
        pl_str = "<Placemark>\n" + \
                 "<name>" + node.get_node_name() + "(" + str(node.get_node_num()) + ")" + "</name>\n" + \
                 "<description>null</description>\n" + \
                 "<styleUrl>#msn_placemark_circle</styleUrl>\n" + \
                 "<Point>\n" + \
                 "<coordinates>" + str(node.get_lon_deg()) + "," + str(node.get_lat_deg()) + ",0 </coordinates>\n" + \
                 "</Point>\n" + \
                 "</Placemark>\n"

        return pl_str

    def __obtain_link_placemark_str(self,link):
        """
        Given a link instance, returns a placemark string

        :param link: Link
        :return: a string of <Placemark>...</Placemark> for link
        """
        node1_num = link.get_start_node_num();
        node2_num = link.get_end_node_num()
        lat1, lon1 = self.nodes[node1_num].get_latlon_deg()
        lat2, lon2 = self.nodes[node2_num].get_latlon_deg()
        link_lat = (lat1 + lat2) / 2.0;
        link_lon = (lon1 + lon2) / 2.0

        pl_str = "<Placemark>\n" + \
                 "<name>" + link.get_link_name() + "</name>\n" + \
                 "<description>null</description>\n" + \
                 "<styleUrl>#msn_placemark_arrow</styleUrl>\n" + \
                 "<MultiGeometry>\n" + \
                 "<Point>\n" + \
                 "<coordinates>" + str(link_lon) + "," + str(link_lat) + ",0 </coordinates>\n" + \
                 "</Point>\n" + \
                 "<LineString>\n" + \
                 "<tessellate>0</tessellate>\n" + \
                 "<coordinates>" + str(lon1) + "," + str(lat1) + ",0" + str(lon2) + "," + str(
            lat2) + ",0" + "</coordinates>\n" + \
                 "</LineString>\n" + \
                 "</MultiGeometry>\n" + \
                 "</Placemark>\n"

        return pl_str

    def __get_kml_style(self):
        """
        For airport, returns a header string for writing a kml file in Google My Maps display
        To change markers and colors, the property must be changed here.

        :return: header of kml file that specifies marker styles
        """
        name_str = '<name>GoogleEarth2_' + self.get_airport_name() + "</name>\n"

        #The following specifies how nodes and links are displayed in My Maps.
        header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + \
                 "<kml xmlns=\"http://earth.google.com/kml/2.2\">\n" + \
                 "<Document xmlns = \"\" >\n" + \
                 name_str + \
                 "<StyleMap id = \"msn_placemark_circle\" >\n" + \
                 "<Pair>\n" + \
                 "<key> normal </key>\n" + \
                 "<styleUrl>#sn_placemark_circle</styleUrl>\n" + \
                 "</Pair>\n" + \
                 "<Pair>\n" + \
                 "<key>highlight</key>\n" + \
                 "<styleUrl>#sh_placemark_circle_highlight</styleUrl>\n" + \
                 "</Pair>\n" + \
                 "</StyleMap>\n" + \
                 "<Style id=\"sn_placemark_circle\">\n" + \
                 "<IconStyle>\n" + \
                 "<color>e61bf5ff</color>\n" + \
                 "<scale>1</scale>\n" + \
                 "<Icon>\n" + \
                 "<href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>\n" + \
                 "</Icon>\n" + \
                 "</IconStyle>\n" + \
                 "<LineStyle/>\n" + \
                 "</Style>\n" + \
                 "<Style id = \"sh_placemark_circle_highlight\" >\n" + \
                 "<IconStyle>\n" + \
                 "<color>e61bf5ff</color>\n" + \
                 "<scale>1.5</scale>\n" + \
                 "<Icon>\n" + \
                 "<href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href>\n" + \
                 "</Icon>\n" + \
                 "</IconStyle>\n" + \
                 "<LineStyle/>\n" + \
                 "</Style>\n" + \
                 "<StyleMap id =\"msn_placemark_arrow\">\n" + \
                 "<Pair>\n" + \
                 "<key>normal</key>\n" + \
                 "<styleUrl>#sn_placemark_arrow</styleUrl>\n" + \
                 "</Pair>\n" + \
                 "<Pair>\n" + \
                 "<key>highlight</key>\n" + \
                 "<styleUrl>#sh_placemark_arrow_highlight</styleUrl>\n" + \
                 "</Pair>\n" + \
                 "</StyleMap>\n" + \
                 "<Style id =\"sn_placemark_arrow\"> \n" + \
                 "<IconStyle>\n" + \
                 "<color> 80ffffff </color>\n" + \
                 "<scale> 0.3 </scale>\n" + \
                 "<Icon>\n" + \
                 "<href>http://maps.google.com/mapfiles/kml/shapes/arrow.png </href >\n" + \
                 "</Icon>\n" + \
                 "</IconStyle>\n" + \
                 "<LineStyle>\n" + \
                 "<color>e61bf5ff</color>\n" + \
                 "<width>2</width>\n" + \
                 "</LineStyle>\n" + \
                 "</Style>\n" + \
                 "<Style id =\"sh_placemark_arrow_highlight\">\n" + \
                 "<IconStyle>\n" + \
                 "<color>80ffffff</color>\n" + \
                 "<scale>0.5</scale>\n" + \
                 "<Icon>\n" + \
                 "<href>http://maps.google.com/mapfiles/kml/shapes/arrow.png</href>\n" + \
                 "</Icon>\n" + \
                 "</IconStyle >\n" + \
                 "<LineStyle>\n" + \
                 "<color>e61bf5ff</color>\n" + \
                 "<width>2</width>\n" + \
                 "</LineStyle>\n" + \
                 "</Style>"

        return header

class Utils:
    """
    Collection of utility functions
    """

if __name__=='__main__':

    #1. plot backgrounds, US map, center, sector

    centerfile = './data/Centers_CONUS'
    #in Default, include center boundaries
    center_handle = RegionHandler()
    center_handle.read_region_file(centerfile,'CENTER')
    include_sector=False
    if include_sector:
        sectorfile = './data/SectorData'  # large file. takes time in loading and plotting
        sector_handle = RegionHandler()
        sector_handle.read_region_file(sectorfile,'SECTOR')

    #2.output xmlfile
    fname='output_trajectory_ex.xml'
    
	#3.Read Output File
    oh=OutFileHandler() #empty (for ease of background plot testing)
    if fname.endswith('xml'):
        oh.read_xml_file(fname) #read xml file
    elif fname.endswith('h5'):
        oh.read_hdf5_file(fname)
    elif fname.endswith('csv'):
        oh.read_csv_file(fname)
    else:
        raise NameError('The file type of {} is not supported'.format(fname))

    #3. collect PHX departing trajectories
    #callsigns_of_interest=oh.get_callsigns_departing_from('SFO')
    #callsigns_of_interest=oh.get_callsigns_departing_from('PHX')
    # no PHX arriving trajectories in the above example
    #no SFO arriving trajectories
    #callsigns_of_interest = oh.get_trajectories_arriving_at('SFO')
    callsigns_of_interest=oh.get_all_callsigns()

    #4. plot with or without background

    fig=plt.figure(0)
    fig.set_size_inches(9 * 12 / 7, 9)
    ax0 = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax0.set_facecolor('black')
    #a.center plot and/or sector plot
    center_handle.plot_regions(plt,color='w')
    if include_sector: #takes long time to plot
        sector_handle.plot_regions(plt,color='w')
    #b. plot trajectories of interest
    oh.plot_trajectories_from_callsigns(callsigns_of_interest,plt)

    plt.show()


