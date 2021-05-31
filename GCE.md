# 🖥️ Deploy to Google Compute Engine

You can apply this application to the Google Cloud Platform Compute Engine. Following are the steps for running this application in a Virtual Machine on Compute Engine.

## 📌Set up Google Cloud Platform

**1. Open a Google Cloud Platform account.**

If you're new to Google Cloud, you can [create an account](https://console.cloud.google.com/freetrial) and new customers also get $300 in free credits to run, test, and deploy workloads.

**2. In the Google Cloud Console, on the project selector page, select or create a Google Cloud projec**

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard) to select a project.

**3. Make sure that billing is enabled for your Cloud project**

[learn how to confirm that billing is enabled for your project](https://cloud.google.com/billing/docs/how-to/modify-project)

**4. Enable the Compute Engine API**

[Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=compute) then select the project used.


## 📌Set up Compute Engine

**1. Create Virtual Machine (VM) Instance**

Following the step how to create a [virtual machine (VM) instance](https://cloud.google.com/compute/docs/instances/create-start-instance)

You can also be following settings like this⬇️

![image](https://drive.google.com/uc?export=view&id=1SUlHvpseOwX9uDCBj3AG6niYGQVF2CCt)

**2. Crate Firewall Rule**

Following the step how to create [firewall rule](https://cloud.google.com/vpc/docs/using-firewalls)

<b>Note</b> : add this in some specific field ⬇️

| Field | Value | Additional Information  |
| :---:   | :-: | :-: |
| Target tags | [Your-Tag] | will be used in the next step |
| Source IP ranges | [Your-External IP] | replacing with the Exernal IP address of your VMs|
| Tcp | 8000 | firewall rule that allows all incoming traffic on tcp:8000 |


**3. Edit Network tags of VMs**

- First click 'Edit' in vms
- Add the tag that you created before in the network tags field (don't forget add http-server and https-server)

![image](https://drive.google.com/uc?export=view&id=1MKCBXd0MrZkwjk-itcelX9_LOcC5abu6)

**4. Change External IP Type**

- In the navigation menu click 'VPC Network'
- and then click 'External IP addresses'
- Change Type External IP to static, like the example below⬇️

![image](https://drive.google.com/uc?export=view&id=1Jk5pGgdZ2uRzgAtt7RGHda7ZSj_aW-DK)


## 📌Set up SQL

**1. Creating a Cloud SQL instance**

Following the step how to create a [Cloud SQL for MySQL Second Generation instance](https://cloud.google.com/sql/docs/mysql/create-instance)**


**2. Create a Cloud SQL User**

Following the step how to create a [new user by using the Cloud Console](https://cloud.google.com/sql/docs/mysql/create-manage-users#creating) for your Cloud SQL instance

**3. Create a Cloud SQL Database**

Following the step how to create a [new database by using the Cloud Console](https://cloud.google.com/sql/docs/mysql/create-manage-databases#create) for your Cloud SQL instance


**3. Create a network path for connecting to SQL instance**

- first click 'Connection' in sql
- And then click 'Add Network' on 'Authorized networks'

| Field | Value | Additional Information  |
| :---:   | :-: | :-: |
| Name| [Network-Name] | custom network name |
| Network | [Your-External IP] | replacing with the Exernal IP address of your VMs|


## 📌Set up the application on VM Instances

**1. Click SSH**

**2.Login as SuperUser and go to /home folder**

```bass
sudo su
cd ..
```

**3. Set Up Python environment, including Python, `pip`, and `virtualenv`**

```bass
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

**4. Clone project from repository github**

```bass
git clone https://github.com/SVeeIS/kotliteProjectAPI.git
```

**5. Go to directory project**

```bass
cd kotliteProjectAPI
```

**6. Create an isolated Python environment, and install django**

```bass
virtualenv env -p python3
source env/bin/activate
pip install django
```

**7. install dependencie and tensorflow**

Open **`requirements.txt`** for editing.

```bass
sudo vim requirements.txt
```

comment on **`tensorflow==2.5.0`** and **`tensorflow-estimator==2.5.0`**

```bass
pip install --no-cache-dir tensorflow
pip install -r requirements.txt
```

**8. Configuring **`settings.py`****


- Open **`kotliteProjectAPI/settings.py`** for editing.

```bass
sudo vim kotliteProjectAPI/settings.py
```

<b>Note : </b> To **`editing file`**  type **`i`** and to **`save file`** type **`:wq`**

Uncomment this section of the file **`settings.py`**

```python
# UNCOMMENT THIS CODE FOR SETUP IN GCP
# import pymysql  # noqa: 402
# pymysql.version_info = (1, 4, 0, 'final', 0)  # change mysqlclient version
# pymysql.install_as_MySQLdb()


# [START db_setup]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '[YOUR-PUBLIC-IP-SQL-INSTANCE]',
#         'USER': '[YOUR-USERNAME]',
#         'PASSWORD': '[YOUR-PASSWORD]',
#         'NAME': '[YOUR-DATABASE]',
#     }
# }
# [END db_setup]
```

**become the example below⬇️**

```python
# UNCOMMENT THIS CODE FOR SETUP IN GCP
import pymysql  # noqa: 402
pymysql.version_info = (1, 4, 0, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()


# [START db_setup]
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'HOST': '[YOUR-PUBLIC-IP-SQL-INSTANCE]',
         'USER': '[YOUR-USERNAME]',
         'PASSWORD': '[YOUR-PASSWORD]',
         'NAME': '[YOUR-DATABASE]',
     }
 }
# [END db_setup]
```

Save **`settings.py`**


**9. Configuring **`maps_env.py`****

- Open **`maps_env.py`** for editing.

```bass
sudo vim maps_env.py
```
change `[YOUR API KEY]` with your Maps API Key

Save **`maps_env.py`**

**10. Run the Django migrations to set up your models**

```bash
python manage.py makemigrations
python manage.py makemigrations drivers
python manage.py makemigrations passengers
python manage.py makemigrations users
python manage.py migrate
```

**11. Create a superuser. You need to define a username and password**

```bash
python manage.py createsuperuser
```

**12. Create a screen and run the application**

- use screen so the application can always run in the background

```bash
screen
source env/bin/activate
python manage.py runserver 0.0.0.0:8000
```

<b>Note:</b> use **`screen -r`** to enter screen already exist and **`ctrl+a d`** to exit from screen
