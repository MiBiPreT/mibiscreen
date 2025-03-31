#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:31:44 2025

@author: alraune
"""
import logging
import sys

def set_logging(where = 'std',
                level = 'INFO',
                ):
    
    '''
    Set logging specifics: written output to users.
    
    Input
    -----
    where: str, default 'std'
        'std' - output to standard stream
        'file' - output to file 'output.log'
    
    Return
    ------
    
    
    '''

    if level == 'INFO':
        log_level=logging.INFO
    elif level == 'DEBUG':
        log_level=logging.DEBUG
    elif level == 'WARNING':
        log_level=logging.WARNING
    elif level == 'ERROR':
        log_level=logging.ERROR
    else:
        log_level=logging.INFO
    
    if where == 'std':     
        logging.basicConfig(stream=sys.stdout,
                            level=log_level
                            )        
    elif where == 'file':
        file_name = 'output.log'
        logging.basicConfig(filename=file_name,
                            encoding='utf-8',
                            level=log_level
                            )