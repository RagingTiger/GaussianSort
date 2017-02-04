## Table of Contents
- [Description](https://github.com/RagingTiger/GaussianSort#description)
- [Installation](https://github.com/RagingTiger/GaussianSort#installation)
- [Usage](https://github.com/RagingTiger/GaussianSort#usage)
  + [Basic](https://github.com/RagingTiger/GaussianSort#basic-usage-printing-to-standard-out)
  + [Advanced](https://github.com/RagingTiger/GaussianSort#advanced-usage-saving-to-output-file)


### Description
The **gausssort** utility was designed to read in output files of the following
format:

```
#Tick Number: 0  #A_bacteria   #B_bacteria    #_bacteria
1 9 20 29
2 11 21 32
3 11 30 41
4 11 39 50
5 13 48 61
6 16 65 81
7 18 80 98
8 21 102 123
9 25 134 159
...
```

Specifically, this includes four entries separated by '&#32' characters
(i.e space characters). **It is NOT currently generalized to work with other
file types**.

For each file it finds in the given path (see [Usage](https://github.com/RagingTiger/GaussianSort#usage) section) it will read in
the data, and calculate the standard deviation for that series of data. Once it
has completed reading all the files it will return a list of file names sorted
in ascending order by standard deviation.


### Installation
Installing the utility from the command line is simple, follow these steps:

```
cd <location_you_want_to_clone_to>
git clone https://github.com/RagingTiger/GaussianSort.git
```

Or if you would prefer to simply [download the repository as a zip file](https://github.com/RagingTiger/GaussianSort):
<p align="center">
  <img src="https://github.com/RagingTiger/images/raw/master/guasssort_download_button.png"/>
</p>

Simply click on the 'green' **Clone or download** button.


### Usage
Currently the utility is not setup to be installed as a global utility. To use
it you must first 'cd' into the **GaussSort** directory:

```
cd GaussSort/
```

Once in the directory **GaussSort** the utility is simple to use, but there are
several options to be aware of:

```
Usage:
  gausssort bact.a <read_file_path> [save [<write_file_path>]]
  gausssort bact.b <read_file_path> [save [<write_file_path>]]
  gausssort bact.total <read_file_path> [save [<write_file_path>]]
```


#### Basic Usage: Printing to Standard Out
First, to clarify, the above usage statement is written in the [docopt](http://docopt.org/) syntax and it is more simple than it appears. The
first word **gausssort** can be ignored, only the other four words need to be
considered. The first of these words is a subcommand specifying which column of
data (i.e. #A_bacteria, #B_bacteria, #\_bacteria stored in each file shown in
the [Description](https://github.com/RagingTiger/GaussianSort#description)
section) to calculate the standard deviation on:

```
bact.a
bact.b
bact.total
```

The next word '\<read_file_path\>' will be the path to the files you want to
sort. For example, if I wanted to launch the utility and sort on the
'#A_bacteria' data in each of the files located in the '/home/gauss/data'
directory:

```
./gausssort.py bact.a /home/gauss/data
```

This usage will print to stdout the file names sorted with their
'gaussian widths' (i.e. standard deviation) next to each name:

```
1:   test-A_0_0.2_0.5_0.5_0.5_0.5.dat        2.62489899361

2:   test-A_0_0.4_0.5_0.5_0.5_0.5.dat        2.62489899361

3:   test-A_0_0.6_0.5_0.5_0.5_0.5.dat        2.62489899361

4:   test-A_0_0.8_0.5_0.5_0.5_0.5.dat        2.62489899361

5:   test-A_0_0_0.5_0.5_0.5_0.5.dat          2.62489899361

6:   test-A_0_1_0.5_0.5_0.5_0.5.dat          2.62489899361

7:   test-A_0.2_0.2_0.5_0.5_0.5_0.5.dat      3.03493910298

8:   test-A_0.2_0.4_0.5_0.5_0.5_0.5.dat      3.03493910298

9:   test-A_0.2_0.6_0.5_0.5_0.5_0.5.dat      3.03493910298

10:  test-A_0.2_0.8_0.5_0.5_0.5_0.5.dat      3.03493910298

...
```


#### Advanced Usage: Saving to Output File

A more advanced usage involves the **save** command:

```
./gausssort.py bact.a /home/gauss/data save
```

This will run the utility and write the output to a file in the **GaussSort**
directory. The output file will be named based on the date and time, and will
therefore be a unique file and not in danger of being overwritten.

Optionally, you can give a name to the output file:

```
./gausssort.py bact.a /home/gauss/data save list_of_gausssorted_filenames.txt
```

This will of course save the output in the 'list_of_gausssorted_filenames.txt'
file.
