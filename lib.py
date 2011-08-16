import traceback
import sys
import smtplib
import syslog
#my oh shit something broke function
def bail():
    info = sys.exc_info()
    exc_type = info[ 0 ]
    exc_value = info[ 1 ]
    exc_traceback = info[ 2 ]
    trace = traceback.extract_tb( sys.exc_traceback )

    error_text = "Exception type: " + str( exc_type ) + "\r\n"
    error_text += "Error message: " + str( exc_value ) + "\r\n"
    error_text += "File name: " + str( trace[ 0 ][ 0 ] ) + "\r\n"
    error_text += "Line: " + str( trace[ 0 ][ 1 ] ) + "\r\n"
    error_text += "Function: " + str( trace[ 0 ][ 2 ] ) + "\r\n"
    error_text += "Line called: " + str( trace[ 0 ][ 3 ] ) + "\r\n"
    log_me(  error_text )

def email_message( to_name, to_addr, from_name, from_addr, subject, msg ):
    to_addr_list = to_addr.split( ";" )
    for addr in to_addr_list:
        if addr:
            headers = ( "From: \"%s\" <%s>\r\nSubject: \"%s\"\r\nTo: \"%s\" <%s>\r\n\r\n"
                % ( str( from_name ), str( from_addr ), str( subject ), str( addr ), str( addr ) ) )
            data = headers + msg
            server = smtplib.SMTP( "mail.news-leader.com:25" )
            #server.starttls()
            #server.login( username, password )
            server.set_debuglevel( 0 )
            server.sendmail( str( from_addr ), str( addr ), data )
            server.quit()

#logs whatever
def log_me( str_in ):
    syslog.openlog( "911_import", 0, syslog.LOG_LOCAL3 )
    syslog.syslog( str_in )
    syslog.closelog()
    print str_in

def get_sql_var( value, var_type=None ):
    """get_sql_var() automagically determines the variable type that needs to be added,
    and returns a SQL worthy string to be added into a query, or a variable type can be
    forced also."""
    
    valid_types = [ "numeric", "string", "date", "bool" ]
    if var_type is not None and var_type not in valid_types:
        raise TypeError, "var_type of \"" + str( var_type ) + "\" is not valid. Must be one of: " + valid_types.join( ", " )
    
    if var_type is None:
        type_cl = type( value )
        # Realistically, with auto-determined types, int and string are the only ones
        if isinstance( type_cl, int ) or isinstance( type_cl, float ):
            var_type = "numeric"
        else:
            # This could be separated out to determine bools etc but that's pointless as bool and string are so similar
            var_type = "string"
            
    if var_type == "numeric":
        # After some debating, I'm not going to catch an exception here, since I would only 
        # need to re-raise effectively the same error after it was caught
        if value is None or value == "":
            retval = "NULL"
        else:
            retval = str( int( value ) )
            
    elif var_type == "bool":
        if value in [ "t", "T", 1, "1", "y", "Y" ]:
            retval = "'t'"
        elif value in [ "f", "F", 0, "0", "n", "N" ]:
            retval = "'f'"
        elif value is None or value.lower() in [ "", "null" ]:
            retval = "NULL"
        else:
            raise ValueError, "Invalid value for variable type 'bool': " + str( repr( value ) )
            
    elif var_type == "date":
        raise NotImplementedError, "Date support will be added in the future; not essential right now"
        
    else:
        # By default, assume string
        if value is None:
            retval = "NULL"
        else:
            # Need to do all kinds of things to make sure this will work as nice clean standard SQL
            retval = str( value )
            retval = retval.replace( "'", "''" )
            retval = "'" + retval + "'"
            
    return retval
