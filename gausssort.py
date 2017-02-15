#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Description:
    Simple utility to read in '.dat' files and measure the gaussian of the data
    and sort the files based on the gaussian width
Dependencies:
    docopt, statistics
Usage:
    gausssort bact.a <read_file_path> [save [<write_file_path>]]
    gausssort bact.b <read_file_path> [save [<write_file_path>]]
    gausssort bact.total <read_file_path> [save [<write_file_path>]]
'''

# libraries
import os
import datetime
import statistics


# functions
def comp_structs(struct):
    return struct.gwidth


def print_data(data):
    print data


# classes
class GaussStruct(object):
    '''
    Class to implement simple 'struct' like object for holding file name and
    standard deviation for data in file
    '''
    def __init__(self, filename, stdev):
        # store
        self.filename = filename
        self.gwidth = stdev

    def __repr__(self):
        return '{0} {1}: object at {2}'.format(self.filename,
                                               self.gwidth,
                                               id(self))


class GaussSort(object):
    '''
    Class to implement storage of data file names / information and sorting
    files on gaussian width
    '''
    def __init__(self, pathtofiles, writepath, save=False):
        # check path for trailing '/'
        if pathtofiles.rsplit('/', 1) == '':
            char = ''
        else:
            char = '/'

        # get list of files
        self.save = save
        self.writepath = writepath
        self.readfilepath = pathtofiles + char
        self.file_list = os.listdir(self.readfilepath)

        # store dict of commands
        self.cmd = {1: 'bact.a', 2: 'bact.b', 3: 'bact.total'}

    def _gaussian_width(self, datafile):
        '''
        Private method to calculate the gaussian width for the data in
        'datafile'
        '''
        # open file
        with open(self.readfilepath + datafile, 'r') as data:
            # discard top line
            data.readline()

            # gen dict
            data_list = []

            # read other lines
            for line in data:
                # strip and split line
                dlist = line.strip('\n').split(' ')

                # gen key and val
                data_list.append(int(dlist[self.index]))

            # calculate stdev
            stdev = statistics.stdev(data_list)

            # return object
            return GaussStruct(datafile, stdev)

    def _data_string(self, dlen, data, func=print_data):

        for i, entry in enumerate(data):
            ilen = dlen + 2 - len(str(i+1))
            nmlen = 40 - len(entry.filename)
            line = '{0}:{1}{2}{3}{4}\n'.format(i+1, ' '*ilen,
                                               entry.filename, ' '*nmlen,
                                               entry.gwidth)
            func(line)

    def _write_data(self, data):
        '''
        Private method to print out data in GaussStructs
        '''
        # chekc for outfile name
        if self.writepath:
            outfile = self.writepath
        else:
            dt = datetime.datetime.now().strftime('%m.%d.%y_%H.%M.%S')
            outfile = 'outfile.{0}.{1}.txt'.format(self.cmd[self.index], dt)

        # write out
        dlen = len(str(len(data)))
        with open(outfile, 'w') as out:
            self._data_string(dlen, data, out.write)

    def _output_data(self, data):
        '''
        Private method to determine ouput source
        '''
        # control flow
        if self.save:
            self._write_data(data)
        else:
            dlen = len(str(len(data)))
            self._data_string(dlen, data)

    def gaussian_sort(self, index):
        '''
        Method to sort data files based on gaussian width (from small to large)
        '''
        # store index
        self.index = index

        # store GaussStructs
        gauss_widths = []

        # get data
        for name in self.file_list:
            # check if hidden file
            if name.split('.')[0] == '':
                continue
            else:
                gauss_widths.append(self._gaussian_width(name))

        # sort widths
        self._output_data(sorted(gauss_widths, key=comp_structs))


# executable
if __name__ == '__main__':

    # executable imports
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # check for output file
    if args['save']:
        if args['<write_file_path>']:
            outfile = args['<write_file_path>']
        else:
            outfile = None
        save = True
    else:
        save = False
        outfile = None

    # global object
    gsort = GaussSort(args['<read_file_path>'], outfile, save)

    # control flow
    if args['bact.a']:
        # call gausssort with index [1]
        gsort.gaussian_sort(1)

    elif args['bact.b']:
        # call gausssort with index [2]
        gsort.gaussian_sort(2)

    elif args['bact.total']:
        # call gausssort with index [3]
        gsort.gaussian_sort(3)
