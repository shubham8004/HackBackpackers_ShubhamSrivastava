#!/usr/bin/env python
# coding: utf-8

# In[165]:


# Import required packages
import xml.etree.ElementTree as ET
import re


# In[166]:


def parse_xml(xml_file_name):
    # Parse XML tree and returns it's root
    tree = ET.parse('wf_src_idw_cntry_multi_def_cd.xml')
    # Get root element
    root = tree.getroot()
    return root


# In[167]:


def parse_transformfield(root, dict_obj):
    # Loop through the iterrable element "TRANSFORMFIELD" as these only contains the transformations embedded in them
    for trans in root.iter('TRANSFORMFIELD'):
        attribute = trans.attrib
        # Consider only those transformfields which has "EXPRESSION" as one of it's attribute
        if 'EXPRESSION' in attribute:
    #         print(attribute)
            # Check if there exists any opening parenthesis in the EXPRESSION attribute
            # If it doesn't exists , this means the transformation function doesn't take any input else it does
            if('(' not in attribute['EXPRESSION']):
                # If Port type is Input/Output then same field is acting as INPUT as well as OUTPUT
                if('INPUT/OUTPUT' in attribute['PORTTYPE']):
                    inp_col = str(attribute['NAME']).strip()
                    trans = str(attribute['EXPRESSION']).strip()
                    out_col = str(attribute['NAME']).strip()
                    print('source(' + inp_col + ') -> transformation(' + trans + ') -> target(' + out_col + ')')
                else: # If Port type is Output then input will be None as the transformation function does not takes in any input
                    inp_col = 'None'
                    trans = str(attribute['EXPRESSION']).strip()
                    out_col = str(attribute['NAME']).strip()
                    print('source(' + inp_col + ') -> transformation(' + trans + ') -> target(' + out_col + ')')
            else:
                # This section means transformation function does take some input
                # Reading text in between '(' and ')'
                match = re.findall(r'\((.*)\)', attribute['EXPRESSION'])
                inp_col = match[0].split(',')[0]
                trans = str(attribute['EXPRESSION']).strip()
                out_col = str(attribute['NAME']).strip()
                print('source(' + inp_col + ') -> transformation(' + trans + ') -> target(' + out_col + ')')
    return dict_obj


# In[168]:


def parse_connectorfield(root, dict_obj):
    for trans in root.iter('CONNECTOR'):
        attribute = trans.attrib
        inp_col = str(attribute['FROMFIELD']).strip()
        trans = str(attribute['FROMINSTANCE']).strip()
        out_col = str(attribute['TOFIELD']).strip()
        print('source(' + inp_col + ') -> transformation(' + trans + ') -> target(' + out_col + ')')
    return dict_obj


# In[169]:


xml_file_name = 'wf_src_idw_cntry_multi_def_cd.xml'
root = parse_xml(xml_file_name)

parse_transformfield(root, dict_obj)
parse_connectorfield(root, dic_1)

