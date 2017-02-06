anat=$1
source /etc/fsl/5.0/fsl.sh;  bet $anat mp2rage_bet.nii.gz -f 0.3 ; mri_watershed $anat mp2rage_ws.nii.gz ; 3dcalc -overwrite -a $anat -b mp2rage_ws.nii.gz -c mp2rage_bet.nii.gz -expr 'a*step(b+c)' -prefix mp2rage_ns.nii.gz
