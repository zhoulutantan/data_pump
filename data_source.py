# -*- coding: utf-8 -*-
import os
import config as fig


class data_source(object):
    def __init__(self,source_dict,file_access=None):
        self._source_dict = source_dict
        self.file_access = None

    @property
    def get_file_access(self):
        return self.file_access



    def set_file_access(self):
        if(self._source_dict['type']=='text'):
            path=self._source_dict['path']
            file_pre=self._source_dict['file_pre']
            for root, dirs, files in os.walk(path):
                for filename in files:
                    fn=filename
                    if(file_pre in fn and 'validate' not in fn):
                        re_file_name=path+"/"+filename
            self.file_access=re_file_name
        elif(self._source_dict['type']=='url'):
            self.file_access=self._source_dict['url']
        else:
            self.file_access=None


if __name__ == "__main__":
    ds=data_source(fig.lead_ds_dict)
    ds.set_file_access()
    file_name = ds.file_access
    print(file_name)