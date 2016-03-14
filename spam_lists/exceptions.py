# -*- coding: utf-8 -*-
'''
This module contains all classes of exceptions raised
by the library
'''

class SpamListsError(Exception):
    '''There was an error during testing a url or host'''
    
class UnknownCodeError(SpamListsError, KeyError):
    '''The classification code from the service was not recognized'''
    
class UnathorizedAPIKeyError(SpamListsError, ValueError):
    '''The API key used to query the service was not authorized'''
    
class InvalidHostError(SpamListsError, ValueError):
    '''The value is not a valid host'''
    
class InvalidIPv4Error(InvalidHostError):
    '''The value is not a valid IPv4 address'''
    
class InvalidIPv6Error(InvalidHostError):
    '''The value is not a valid IPv6 address'''

class InvalidHostnameError(InvalidHostError):
    '''The value is not a valid hostname'''
    
class InvalidURLError(SpamListsError, ValueError):
    '''The value is not a valid url'''