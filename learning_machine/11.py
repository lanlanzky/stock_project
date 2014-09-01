def backnormal(backdata,outdata):
        large=max(backdata)
        small=min(backdata)
        bizhi=large-small
	for i in range(len(outdata)):
		for j in range(len(outdata[1])):
                        outdata[i][j]=outdata[i][j]*bizhi+small
        return outdata
