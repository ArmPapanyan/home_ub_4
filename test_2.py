from sshcheckers import ssh_checkout_negative, ssh_checkout


import yaml


with open('config.yaml') as f:
   data = yaml.safe_load(f)


class Testneg:
   def test_nstep1(self, make_folders, make_bad_arx):
       # test neg 1
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], "cd {}; 7z e {}.{} -o{} -y".format(data["FOLDER_OUT"], make_bad_arx, data["type"],
                                                                       data["FOLDER_1"]), "ERROR:"), "test1 FAIL"


   def test_nstep2(self, make_bad_arx):
       # test neg 2
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], "cd {}; 7z t {}.{}".format(data["FOLDER_OUT"], make_bad_arx,
                                                               data["type"]), "ERROR:"), "test2 FAIL"


   def test_nstep3(self):
       res = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "echo '{}' | sudo -S dpkg -r"
                                                                         " {}".format(data["passwd"], data["pkgname"]),
                               "Удаляется"))
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "echo '{}' | "
                                                                         "sudo -S dpkg -s {}".format(data["passwd"],
                                                                                                     data["pkgname"]),
                               "Status: deinstall ok"))
       assert all(res), "test3 FAIL"

