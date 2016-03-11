import sys
import babeltrace.reader
import numpy as np
from plotly.offline import plot
import plotly
import plotly.graph_objs as go
import datetime

import tracer

import os

def timestampToDate(timestamp) :
    return  datetime.datetime.fromtimestamp(timestamp / 1e9).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    #help(plotly.offline.plot)
    if len(sys.argv) != 2:
        msg = 'Usage: python {} TRACEPATH'.format(sys.argv[0])
        raise ValueError(msg)
    
    sessions = tracer.getSessions(sys.argv[1])
    i = 0
    for ses in sessions :
        errorString = ''
        if (ses[0]['exitCode'] != 0) :
            errorString = 'NOT COMPLETED'
        
        print( str(i) + " : " + timestampToDate(ses[0]['timestamp']) + " - "+ timestampToDate(ses[1])
              + " : {:.1f}s ".format((ses[1] - ses[0]['timestamp']) / 1000000000) + errorString)
        print( "      Max Pipeline size\t: " + str(ses[0]['maxPipelineSize']))
        print( "      Interest lifetime\t: " + str(ses[0]['interestLifetime']))
        print( "      Max retries      \t: " + str(ses[0]['maxRetries']))
        print( "      Must be fresh    \t: " + str(ses[0]['mustBeFresh']))
        print( "      Exit code        \t: " + str(ses[0]['exitCode']))
        print()
        i += 1
        
    try:
        if len(sessions) > 1 :
            sessionNo = int(input('Insert session number: '))
        else :
            sessionNo = 0;
        if sessionNo >= len(sessions) :
            print("ERROR: no session with specified number")
        else :
            print ("Running with session " + str(sessionNo) + "...")
            tracer.chunksStatistics(sys.argv[1], sessions[sessionNo][0]['timestamp'], sessions[sessionNo][1], 'test ' + timestampToDate(ses[0]['timestamp']))
    except ValueError :
        print("ERROR: Insert a number")