#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.36.2.
# Python 3.8.2 (default, Apr 27 2020, 15:53:34)  [GCC 9.3.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', '/tmp/nfelib/nfelib/v4_00/retConsStatServ.py')
#
# Command line arguments:
#   /tmp/generated/schemas/nfe/v4_00/retConsStatServ_v4.00.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "/tmp/nfelib/nfelib/v4_00/retConsStatServ.py" /tmp/generated/schemas/nfe/v4_00/retConsStatServ_v4.00.xsd
#
# Current working directory (os.getcwd()):
#   v4_00
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class TAmb(str, Enum):
    """Tipo Ambiente"""
    _1='1'
    _2='2'


class TCOrgaoIBGE(str, Enum):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
    _1_1='11'
    _1_2='12'
    _1_3='13'
    _1_4='14'
    _1_5='15'
    _1_6='16'
    _1_7='17'
    _2_1='21'
    _2_2='22'
    _2_3='23'
    _2_4='24'
    _2_5='25'
    _2_6='26'
    _2_7='27'
    _2_8='28'
    _2_9='29'
    _3_1='31'
    _3_2='32'
    _3_3='33'
    _3_5='35'
    _4_1='41'
    _4_2='42'
    _4_3='43'
    _5_0='50'
    _5_1='51'
    _5_2='52'
    _5_3='53'
    _9_0='90'
    _9_1='91'
    _9_2='92'


class TCodUfIBGE(str, Enum):
    """Tipo Código da UF da tabela do IBGE"""
    _1_1='11'
    _1_2='12'
    _1_3='13'
    _1_4='14'
    _1_5='15'
    _1_6='16'
    _1_7='17'
    _2_1='21'
    _2_2='22'
    _2_3='23'
    _2_4='24'
    _2_5='25'
    _2_6='26'
    _2_7='27'
    _2_8='28'
    _2_9='29'
    _3_1='31'
    _3_2='32'
    _3_3='33'
    _3_5='35'
    _4_1='41'
    _4_2='42'
    _4_3='43'
    _5_0='50'
    _5_1='51'
    _5_2='52'
    _5_3='53'


class TMod(str, Enum):
    """Tipo Modelo Documento Fiscal"""
    _5_5='55'
    _6_5='65'


class TUf(str, Enum):
    """Tipo Sigla da UF"""
    AC='AC'
    AL='AL'
    AM='AM'
    AP='AP'
    BA='BA'
    CE='CE'
    DF='DF'
    ES='ES'
    GO='GO'
    MA='MA'
    MG='MG'
    MS='MS'
    MT='MT'
    PA='PA'
    PB='PB'
    PE='PE'
    PI='PI'
    PR='PR'
    RJ='RJ'
    RN='RN'
    RO='RO'
    RR='RR'
    RS='RS'
    SC='SC'
    SE='SE'
    SP='SP'
    TO='TO'
    EX='EX'


class TUfEmi(str, Enum):
    """Tipo Sigla da UF de emissor // acrescentado em 24/10/08"""
    AC='AC'
    AL='AL'
    AM='AM'
    AP='AP'
    BA='BA'
    CE='CE'
    DF='DF'
    ES='ES'
    GO='GO'
    MA='MA'
    MG='MG'
    MS='MS'
    MT='MT'
    PA='PA'
    PB='PB'
    PE='PE'
    PI='PI'
    PR='PR'
    RJ='RJ'
    RN='RN'
    RO='RO'
    RR='RR'
    RS='RS'
    SC='SC'
    SE='SE'
    SP='SP'
    TO='TO'


class xServType(str, Enum):
    """Serviço Solicitado"""
    STATUS='STATUS'


class TConsStatServ(GeneratedsSuper):
    """Tipo Pedido de Consulta do Status do Serviço"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsStatServ', 0, 0, {'use': 'required'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('cUF', ['TCodUfIBGE', 'xs:string'], 0, 0, {'name': 'cUF', 'type': 'xs:string'}, None),
        MemberSpec_('xServ', ['xServType', 'TServ', 'nfe:TString'], 0, 0, {'name': 'xServ', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, tpAmb=None, cUF=None, xServ=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.cUF = cUF
        self.validate_TCodUfIBGE(self.cUF)
        self.cUF_nsprefix_ = None
        self.xServ = xServ
        self.validate_xServType(self.xServ)
        self.xServ_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TConsStatServ)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TConsStatServ.subclass:
            return TConsStatServ.subclass(*args_, **kwargs_)
        else:
            return TConsStatServ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TCodUfIBGE(self, value):
        result = True
        # Validate type TCodUfIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TCodUfIBGE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_xServType(self, value):
        result = True
        # Validate type xServType, a restriction on TServ.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['STATUS']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on xServType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xServType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xServType_patterns_, ))
                result = False
        return result
    validate_xServType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TVerConsStatServ(self, value):
        # Validate type TVerConsStatServ, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerConsStatServ_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerConsStatServ_patterns_, ))
    validate_TVerConsStatServ_patterns_ = [['^(4\\.00)$']]
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.cUF is not None or
            self.xServ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsStatServ', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TConsStatServ')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TConsStatServ':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TConsStatServ')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TConsStatServ', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TConsStatServ'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsStatServ', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.cUF is not None:
            namespaceprefix_ = self.cUF_nsprefix_ + ':' if (UseCapturedNS_ and self.cUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scUF>%s</%scUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cUF), input_name='cUF')), namespaceprefix_ , eol_))
        if self.xServ is not None:
            namespaceprefix_ = self.xServ_nsprefix_ + ':' if (UseCapturedNS_ and self.xServ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxServ>%s</%sxServ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xServ), input_name='xServ')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('versao', node)
        if value is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            self.versao = value
            self.versao = ' '.join(self.versao.split())
            self.validate_TVerConsStatServ(self.versao)    # validate type TVerConsStatServ
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'cUF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cUF')
            value_ = self.gds_validate_string(value_, node, 'cUF')
            self.cUF = value_
            self.cUF_nsprefix_ = child_.prefix
            # validate type TCodUfIBGE
            self.validate_TCodUfIBGE(self.cUF)
        elif nodeName_ == 'xServ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xServ')
            value_ = self.gds_validate_string(value_, node, 'xServ')
            self.xServ = value_
            self.xServ_nsprefix_ = child_.prefix
            # validate type xServType
            self.validate_xServType(self.xServ)
# end class TConsStatServ


class TRetConsStatServ(GeneratedsSuper):
    """Tipo Resultado da Consulta do Status do Serviço"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsStatServ', 0, 0, {'use': 'required'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
        MemberSpec_('cUF', ['TCodUfIBGE', 'xs:string'], 0, 0, {'name': 'cUF', 'type': 'xs:string'}, None),
        MemberSpec_('dhRecbto', ['TDateTimeUTC', 'xs:string'], 0, 0, {'name': 'dhRecbto', 'type': 'xs:string'}, None),
        MemberSpec_('tMed', ['TMed', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'tMed', 'type': 'xs:string'}, None),
        MemberSpec_('dhRetorno', ['TDateTimeUTC', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'dhRetorno', 'type': 'xs:string'}, None),
        MemberSpec_('xObs', ['TMotivo', 'nfe:TString'], 0, 1, {'minOccurs': '0', 'name': 'xObs', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, tpAmb=None, verAplic=None, cStat=None, xMotivo=None, cUF=None, dhRecbto=None, tMed=None, dhRetorno=None, xObs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
        self.cUF = cUF
        self.validate_TCodUfIBGE(self.cUF)
        self.cUF_nsprefix_ = None
        self.dhRecbto = dhRecbto
        self.validate_TDateTimeUTC(self.dhRecbto)
        self.dhRecbto_nsprefix_ = None
        self.tMed = tMed
        self.validate_TMed(self.tMed)
        self.tMed_nsprefix_ = None
        self.dhRetorno = dhRetorno
        self.validate_TDateTimeUTC(self.dhRetorno)
        self.dhRetorno_nsprefix_ = None
        self.xObs = xObs
        self.validate_TMotivo(self.xObs)
        self.xObs_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TRetConsStatServ)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TRetConsStatServ.subclass:
            return TRetConsStatServ.subclass(*args_, **kwargs_)
        else:
            return TRetConsStatServ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TVerAplic(self, value):
        result = True
        # Validate type TVerAplic, a restriction on nfe:TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TVerAplic' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TVerAplic' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerAplic_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerAplic_patterns_, ))
                result = False
        return result
    validate_TVerAplic_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TStat(self, value):
        result = True
        # Validate type TStat, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TStat' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TStat_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TStat_patterns_, ))
                result = False
        return result
    validate_TStat_patterns_ = [['^([0-9]{3})$']]
    def validate_TMotivo(self, value):
        result = True
        # Validate type TMotivo, a restriction on nfe:TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TMotivo' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TMotivo' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TMotivo_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TMotivo_patterns_, ))
                result = False
        return result
    validate_TMotivo_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TCodUfIBGE(self, value):
        result = True
        # Validate type TCodUfIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TCodUfIBGE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TDateTimeUTC(self, value):
        result = True
        # Validate type TDateTimeUTC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TDateTimeUTC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TDateTimeUTC_patterns_, ))
                result = False
        return result
    validate_TDateTimeUTC_patterns_ = [['^((((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d([\\-,\\+](0[0-9]|10|11):00|([\\+](12):00)))$']]
    def validate_TMed(self, value):
        result = True
        # Validate type TMed, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TMed_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TMed_patterns_, ))
                result = False
        return result
    validate_TMed_patterns_ = [['^([0-9]{1,4})$']]
    def validate_TVerConsStatServ(self, value):
        # Validate type TVerConsStatServ, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerConsStatServ_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerConsStatServ_patterns_, ))
    validate_TVerConsStatServ_patterns_ = [['^(4\\.00)$']]
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.verAplic is not None or
            self.cStat is not None or
            self.xMotivo is not None or
            self.cUF is not None or
            self.dhRecbto is not None or
            self.tMed is not None or
            self.dhRetorno is not None or
            self.xObs is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsStatServ', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TRetConsStatServ')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TRetConsStatServ':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TRetConsStatServ')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TRetConsStatServ', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TRetConsStatServ'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsStatServ', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.verAplic is not None:
            namespaceprefix_ = self.verAplic_nsprefix_ + ':' if (UseCapturedNS_ and self.verAplic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverAplic>%s</%sverAplic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verAplic), input_name='verAplic')), namespaceprefix_ , eol_))
        if self.cStat is not None:
            namespaceprefix_ = self.cStat_nsprefix_ + ':' if (UseCapturedNS_ and self.cStat_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scStat>%s</%scStat>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cStat), input_name='cStat')), namespaceprefix_ , eol_))
        if self.xMotivo is not None:
            namespaceprefix_ = self.xMotivo_nsprefix_ + ':' if (UseCapturedNS_ and self.xMotivo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxMotivo>%s</%sxMotivo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xMotivo), input_name='xMotivo')), namespaceprefix_ , eol_))
        if self.cUF is not None:
            namespaceprefix_ = self.cUF_nsprefix_ + ':' if (UseCapturedNS_ and self.cUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scUF>%s</%scUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cUF), input_name='cUF')), namespaceprefix_ , eol_))
        if self.dhRecbto is not None:
            namespaceprefix_ = self.dhRecbto_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRecbto_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRecbto>%s</%sdhRecbto>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dhRecbto), input_name='dhRecbto')), namespaceprefix_ , eol_))
        if self.tMed is not None:
            namespaceprefix_ = self.tMed_nsprefix_ + ':' if (UseCapturedNS_ and self.tMed_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stMed>%s</%stMed>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tMed), input_name='tMed')), namespaceprefix_ , eol_))
        if self.dhRetorno is not None:
            namespaceprefix_ = self.dhRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRetorno_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRetorno>%s</%sdhRetorno>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dhRetorno), input_name='dhRetorno')), namespaceprefix_ , eol_))
        if self.xObs is not None:
            namespaceprefix_ = self.xObs_nsprefix_ + ':' if (UseCapturedNS_ and self.xObs_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxObs>%s</%sxObs>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xObs), input_name='xObs')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('versao', node)
        if value is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            self.versao = value
            self.versao = ' '.join(self.versao.split())
            self.validate_TVerConsStatServ(self.versao)    # validate type TVerConsStatServ
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'verAplic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verAplic')
            value_ = self.gds_validate_string(value_, node, 'verAplic')
            self.verAplic = value_
            self.verAplic_nsprefix_ = child_.prefix
            # validate type TVerAplic
            self.validate_TVerAplic(self.verAplic)
        elif nodeName_ == 'cStat':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cStat')
            value_ = self.gds_validate_string(value_, node, 'cStat')
            self.cStat = value_
            self.cStat_nsprefix_ = child_.prefix
            # validate type TStat
            self.validate_TStat(self.cStat)
        elif nodeName_ == 'xMotivo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xMotivo')
            value_ = self.gds_validate_string(value_, node, 'xMotivo')
            self.xMotivo = value_
            self.xMotivo_nsprefix_ = child_.prefix
            # validate type TMotivo
            self.validate_TMotivo(self.xMotivo)
        elif nodeName_ == 'cUF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cUF')
            value_ = self.gds_validate_string(value_, node, 'cUF')
            self.cUF = value_
            self.cUF_nsprefix_ = child_.prefix
            # validate type TCodUfIBGE
            self.validate_TCodUfIBGE(self.cUF)
        elif nodeName_ == 'dhRecbto':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dhRecbto')
            value_ = self.gds_validate_string(value_, node, 'dhRecbto')
            self.dhRecbto = value_
            self.dhRecbto_nsprefix_ = child_.prefix
            # validate type TDateTimeUTC
            self.validate_TDateTimeUTC(self.dhRecbto)
        elif nodeName_ == 'tMed':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tMed')
            value_ = self.gds_validate_string(value_, node, 'tMed')
            self.tMed = value_
            self.tMed_nsprefix_ = child_.prefix
            # validate type TMed
            self.validate_TMed(self.tMed)
        elif nodeName_ == 'dhRetorno':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dhRetorno')
            value_ = self.gds_validate_string(value_, node, 'dhRetorno')
            self.dhRetorno = value_
            self.dhRetorno_nsprefix_ = child_.prefix
            # validate type TDateTimeUTC
            self.validate_TDateTimeUTC(self.dhRetorno)
        elif nodeName_ == 'xObs':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xObs')
            value_ = self.gds_validate_string(value_, node, 'xObs')
            self.xObs = value_
            self.xObs_nsprefix_ = child_.prefix
            # validate type TMotivo
            self.validate_TMotivo(self.xObs)
# end class TRetConsStatServ


GDSClassesMapping = {
    'retConsStatServ': TRetConsStatServ,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsStatServ'
        rootClass = TRetConsStatServ
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsStatServ'
        rootClass = TRetConsStatServ
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsStatServ'
        rootClass = TRetConsStatServ
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsStatServ'
        rootClass = TRetConsStatServ
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from retConsStatServ import *\n\n')
        sys.stdout.write('import retConsStatServ as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.portalfiscal.inf.br/nfe': [('TCodUfIBGE',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCodMunIBGE',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TChNFe',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TProt',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TRec', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TStat',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpj',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpjVar',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpjOpc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCpf', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TCpfVar',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0104v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0204v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0304Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0803v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1110v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1203',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204temperatura',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1302',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1302Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeDest',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeDestNaoIsento',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeST',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIe', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TMod', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TNF', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TSerie',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TUf', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TUfEmi',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TAmb', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TVerAplic',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TMotivo',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TJust',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TServ',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('Tano', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TMed', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TString',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TData',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TTime',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDateTimeUTC',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TPlaca',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCOrgaoIBGE',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TVerConsStatServ',
                                         'leiauteConsStatServ_v4.00.xsd',
                                         'ST'),
                                        ('TConsStatServ',
                                         'leiauteConsStatServ_v4.00.xsd',
                                         'CT'),
                                        ('TRetConsStatServ',
                                         'leiauteConsStatServ_v4.00.xsd',
                                         'CT')]}

__all__ = [
    "TConsStatServ",
    "TRetConsStatServ"
]
