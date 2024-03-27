ctlid=2403262019
dockertag=jgwill/dev:openaihub

containername=jgtaihub
dkhostname=$containername

# PORT
dkport=8080:8080

xmount=/b/Dropbox/etc/openai/hubconfig:/opt/openai-hub/config
xmount2=/var/log/jgt:/var/log/jgt


#dkcommand=bash #command to execute (default is the one in the dockerfile)

#dkextra=" -v \$dworoot/x:/x -p 2288:2288 "
dkextra="   "
#dkmounthome=true


##########################
############# RUN MODE
#dkrunmode="bg" #default fg
#dkrestart="--restart" #default
#dkrestarttype="unless-stopped" #default


#########################################
################## VOLUMES
#dkvolume="myvolname220413:/app" #create or use existing one
#dkvolume="$containername:/app" #create with containername name



#dkecho=true #just echo the docker run


# Use TZ
#DK_TZ=1



#####################################
#Build related
#
##chg back to that user
#dkchguser=vscode

######################## HOOKS BASH
### IF THEY EXIST, THEY are Executed, you can change their names

dkbuildprebuildscript=dkbuildprebuildscript.sh
dkbuildbuildsuccessscript=dkbuildbuildsuccessscript.sh
dkbuildfailedscript=dkbuildfailedscript.sh
dkbuildpostbuildscript=dkbuildpostbuildscript.sh

###########################################
# Unset deprecated
unset DOCKER_BUILDKIT

