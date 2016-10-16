#!/usr/lib/python
#coding = utf-8
import argparse

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands')
    
    # A list service command
    list_service_parser = subparsers.add_parser(
        'list_service', help='List All Service')
    list_service_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='end')
    list_service_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='the right list service end')
    list_service_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'end')
    list_service_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'end')
    list_service_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='end')
    list_service_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='end')
    
    # A list API command
    list_api_parser = subparsers.add_parser(
        'list_api',help='list all api of the right service ')
    list_api_parser.add_argument( 
        'service_name',action='store',
        help='give the right service name')
    list_api_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='end')
    list_api_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='end')
    list_api_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'the right list api end')
    list_api_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'end')
    list_api_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='end')
    list_api_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='end')

    #A get API command
    get_api_parser = subparsers.add_parser(
        'get_api',help='get the right api')
    get_api_parser.add_argument(
	'service_name',action='store')
    get_api_parser.add_argument(
	'api_name',action='store')
    get_api_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='end')
    get_api_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='end')
    get_api_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'end')
    get_api_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'the right get api end')
    get_api_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='end')
    get_api_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='end')
    
    #A modify API command
    modify_api_parser = subparsers.add_parser(
        'modify_api',help='modify the right api')
    modify_api_parser.add_argument(
        'service_name',action='store')
    modify_api_parser.add_argument(
        'api_name',action='store')
    modify_api_parser.add_argument(
        'param1',action='store')
    modify_api_parser.add_argument(
        'param2',action='store')
    modify_api_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='the right modify api end')
    modify_api_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='end')
    modify_api_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'end')
    modify_api_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'end')
    modify_api_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='end')
    modify_api_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='end')

    #A online API command
    online_api_parser = subparsers.add_parser(
        'online_api',help='online the right api')
    online_api_parser.add_argument(
        'service_name',action='store')
    online_api_parser.add_argument(
        'api_name',action='store')
    online_api_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='end')
    online_api_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='end')
    online_api_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'end')
    online_api_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'end')
    online_api_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='the right online api end')
    online_api_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='end')
    
    #A offline API command
    offline_api_parser = subparsers.add_parser(
        'online_api',help='online the right api')
    offline_api_parser.add_argument(
        'service_name',action='store')
    offline_api_parser.add_argument(
        'api_name',action='store')
    offline_api_parser.add_argument(
        '--modify_api_end','-ma',default=False,action='store_true',help='end')
    offline_api_parser.add_argument(
        '--service_end','-ls',default=False,action='store_true',help='end')
    offline_api_parser.add_argument(
        '--api_end','-la',default = False,action = 'store_true', help = 'end')
    offline_api_parser.add_argument(
        '--get_api_end','-ga',default=False,action = 'store_true',help = 'end')
    offline_api_parser.add_argument(
        '--online_api_end','-oa',default=False,action='store_true',help='end')
    offline_api_parser.add_argument(
        '--offline_api_end','-ofa',default=False,action='store_true',help='the right offline api end')
    
    results = parser.parse_args()
    print results
    if results.service_end:
        print 'servcie'
    if results.api_end:
        print 'api'
    if results.get_api_end:
        print 'get api'

if __name__ == "__main__":
    main()
