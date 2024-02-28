import re

class myconfig:
    # default values
    def __init__(self):
        self.ipx = "192.168.1.247"
        self.portx = 1255
        self.wtitle = "Radio"
        self.mygeometry_w = "361"
        self.mygeometry_h = "601"
        self.pid = "-1904256314"
        self.heos_prefix = "heos://browse/play_stream?pid=%s&url=" % self.pid
    
    def extract_IP(self, text):
        ipx_pattern = r'ipx\s+:\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
        ipx = re.findall(ipx_pattern, text)
        return ipx[0]

    def extract_digit(self, name, alltext):
        d_pattern =  r'{}\s+:\s+(\d+)'.format(name)
        d_res = re.findall(d_pattern, alltext)
        return int(d_res[0])

    def extract_text(self, name, text):
        text_pattern =  r'{}\s+:\s+(\w+)'.format(name)
        text = re.findall(text_pattern, text)
        return text[0]

    def extract_pid(self, text):
        pid_pattern =  r'pid\s+:\s+(-?\d+)'
        pid = re.findall(pid_pattern, text)
        return pid[0]

    def vimport(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Loop through each line in the file
            for I, line in enumerate(lines):
                if 'ipx' in line:
                    self.ipx = self.extract_IP(line)
                elif 'portx' in line:
                    self.portx = self.extract_digit('portx',line)
                elif 'title' in line:
                    self.wtitle = self.extract_text("window title",line)
                elif 'portx' in line:
                    self.portx = self.extract_digit('portx',line)
                elif 'mygeometry_w' in line:
                    self.mygeometry_w = self.extract_digit('mygeometry_w',line)
                elif 'mygeometry_h' in line:
                    self.mygeometry_h = self.extract_digit('mygeometry_h',line)
                elif 'pid' in line:
                    self.pid = self.extract_pid(line)

            self.heos_prefix = "heos://browse/play_stream?pid=%s&url=" % self.pid