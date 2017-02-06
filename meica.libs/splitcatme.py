import nibabel as nib
#import pylab as P
import glob
from sys import stdout,argv
import sys

from string import rstrip,split
#Filename parser for NIFTI and AFNI files
def dsprefix(idn):
	def prefix(datasetname):
		return split(datasetname,'+')[0]
	if len(split(idn,'.'))!=0:
		if split(idn,'.')[-1]=='HEAD' or split(idn,'.')[-1]=='BRIK' or split(idn,'.')[-2:]==['BRIK','gz']:
			return prefix(idn)
		elif split(idn,'.')[-1]=='nii' and not split(idn,'.')[-1]=='nii.gz':
			return '.'.join(split(idn,'.')[:-1])
		elif split(idn,'.')[-2:]==['nii','gz']:
			return '.'.join(split(idn,'.')[:-2])
		else:
			return prefix(idn)
	else:
		return prefix(idn)

def dssuffix(idna):
	suffix = idna.split(dsprefix(idna))[-1]
	#print suffix
	spl_suffix=suffix.split('.')
	#print spl_suffix
	if len(spl_suffix[0])!=0 and spl_suffix[0][0] == '+': return spl_suffix[0]
	else: return suffix



#%matplotlib inline
def niwrite(data,affine, name , header=None):
        stdout.write(" + Writing file: %s ...." % name) 
        
        thishead = header
        if thishead == None:
                thishead = head.copy()
                thishead.set_data_shape(list(data.shape))

        outni = nib.Nifti1Image(data,affine,header=thishead)
        outni.to_filename(name)
        print 'done.'

#vol = nib.load(glob.glob('*.nii')[0])
vol = nib.load(sys.argv[1])
dat = vol.get_data()
aff = vol.get_affine()
head = vol.get_header()

ne=int(sys.argv[2]); 
es = [int(nn) for nn in sys.argv[2:]]
ne = len(es)

meseries = [[tt*ne+ei for tt in range(dat.shape[-1]/ne)] for ei in range(ne)]

for ii in range(len(es)):
	io = es[ii]
	niwrite(dat[:,:,:,meseries[ii]],aff,'%s_e%i.nii' % (dsprefix(argv[1]),io),header=head)
