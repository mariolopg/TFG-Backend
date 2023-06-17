from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
import json
import re
import os

# Create your views here.
@csrf_exempt
def ApiRoot(request, component):

    hardware_testing = []

    if component == 'cpus':
        hardware_testing = scrap_cpus()
    elif component == 'motherboards':
        hardware_testing = scrap_motherboards()
    elif component == 'gpus':
        hardware_testing = scrap_gpus()
    elif component == 'rams':
        hardware_testing = scrap_rams()
    elif component == 'hdds':
        hardware_testing = scrap_hdds()
    elif component == 'ssds':
        hardware_testing = scrap_ssds()
    elif component == 'psus':
        hardware_testing = scrap_psus()
    elif component == 'coolers':
        hardware_testing = scrap_coolers()
    elif component == 'cases':
        hardware_testing = scrap_cases()

    return JsonResponse(hardware_testing, safe = False)

def scrap_cpus():
    cpus = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/cpus')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        cpu = get_cpu_specs(item)
        cpus.append(cpu)

    save_json('cpus', cpus)
    return cpus

def scrap_motherboards():
    motherboards = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/motherboards')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        motherboard_url = item.find_all('a')[0]['href']
        r = requests.get(motherboard_url)

        if r.ok:
            motherboard = BeautifulSoup(r.content, 'html.parser')
            motherboard = get_motherboard_specs(motherboard)
            motherboards.append(motherboard)

        r.close()

    save_json('motherboards', motherboards)
    return motherboards

def scrap_gpus():
    gpus = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/gpus')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        gpu_url = item.find_all('a')[0]['href']
        r = requests.get(gpu_url)

        if r.ok:
            gpu = BeautifulSoup(r.content, 'html.parser')
            series = item.find('span', class_ = 'series').text
            gpu = get_gpu_specs(gpu)
            gpu['series'] = series
            gpus.append(gpu)

        r.close()

    save_json('gpus', gpus)    
    return gpus

def scrap_rams():
    rams = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/rams')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        ram = get_ram_specs(item)
        rams.append(ram)

    save_json('rams', rams)
    return rams

def scrap_hdds():
    hdds = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/hdds')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        hdd = get_hdd_specs(item)
        hdds.append(hdd)

    save_json('hdds', hdds)
    return hdds

def scrap_ssds():
    ssds = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/ssds')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        ssd = get_ssd_specs(item)
        ssds.append(ssd)

    save_json('ssds', ssds)
    return ssds

def scrap_psus():
    psus = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/psus')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        psu_url = item.find_all('a')[0]['href']
        r = requests.get(psu_url)

        if r.ok:
            psu = BeautifulSoup(r.content, 'html.parser')
            psu = get_psu_specs(psu)
            if not(re.findall(r'[\bextern|\bredundant|\bmisc|\bitx]', psu['size']) or psu['size'] == ''):
                psus.append(psu)

        r.close()

    save_json('psus', psus)    
    return psus

def scrap_coolers():
    coolers = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/cpucoolers')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        cooler_url = item.find_all('a')[0]['href']
        r = requests.get(cooler_url)

        if r.ok:
            cooler = BeautifulSoup(r.content, 'html.parser')

            if item.find('span', class_ = 'radiator'):
                cooler = get_liquid_cooler_specs(cooler)
            else:
                cooler = get_air_cooler_specs(cooler)

            coolers.append(cooler)

        r.close()

    save_json('coolers', coolers)  
    return coolers

def scrap_cases():
    cases = []
    hardware_list = get_hardware_list('https://www.pc-kombo.com/us/components/cases')

    for item in hardware_list:
        # * Cuando haya DB comprobar si existe el nombre ---- 'True' => Skip | 'False' => Scrap
        case_url = item.find_all('a')[0]['href']
        r = requests.get(case_url)

        if r.ok:
            case = BeautifulSoup(r.content, 'html.parser')
            case = get_case_specs(case)
            cases.append(case)

        r.close()

    save_json('cases', cases)    
    return cases

def get_hardware_list(url):
    r = requests.get(url)
    hardware_list = []

    if r.ok:
        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')
        hardware_list = soup.find('ol', id = 'hardware').find_all('li')
    
    r.close()
    return hardware_list

def save_json(filename, hardware):
    filename = f"./hardware_json/{filename}.json"
    os.makedirs(os.path.dirname(filename), exist_ok = True)
    with open(filename, 'w') as outfile:
        outfile.write(json.dumps(hardware, indent=2))

def get_spec(specs, spec_to_find, alternative = ''):
    spec = specs.find('dt', text = spec_to_find).find_next_sibling('dd').text

    if alternative != '' and (spec == '' or spec == '0'):
        spec = alternative

    return spec

def get_cpu_specs(cpu):
    specs = {}
    specs['name'] = cpu.find('h5', class_ = 'name').text
    specs['socket'] = cpu.find('span', class_ = 'socket').text
    specs['cores'] = cpu.find('span', class_ = 'cores').text
    threads = cpu.find(text = re.compile(r'\d+ Threads'))
    specs['threads'] = re.findall('\d+', threads )[0]

    print(specs['name'])
    return specs

def get_motherboard_specs(motherboard):
    specs = {}

    specs['name'] = motherboard.find('h1', itemprop = 'name').text
    specs['form_factor'] = get_spec(motherboard, 'Form Factor', 'ATX')
    specs['socket'] = get_spec(motherboard, 'Socket')
    specs['chipset'] = get_spec(motherboard, 'Chipset')
    specs['memory_type'] = get_spec(motherboard, 'Memory Type')
    specs['ram_capacity'] = get_spec(motherboard, 'Memory Capacity', '32')
    specs['ram_slots'] = get_spec(motherboard, 'Ramslots', '2')
    specs['sata_slots'] = get_spec(motherboard, 'SATA', '4')
    specs['m2_3_slots'] = get_spec(motherboard, 'M.2 (PCI-E 3.0)', '0')
    specs['m2_4_slots'] = get_spec(motherboard, 'M.2 (PCI-E 4.0)', '0')

    return specs

def get_gpu_specs(gpu):
    specs = {}
    specs['name'] = gpu.find('h1', itemprop = 'name').text
    specs['vram'] = re.findall('\d+', get_spec(gpu, 'Vram', '8'))[0]
    specs['tdp'] = re.findall('\d+', get_spec(gpu, 'TDP', '100'))[0]
    specs['length'] = re.findall('\d+', get_spec(gpu, 'Length'))[0]
    specs['8_pin_connectors'] = get_spec(gpu, '8-pin connectors', '0')
    specs['6_pin_connectors'] = get_spec(gpu, '6-pin connectors', '0')

    print(specs['name'])
    return specs

def get_ram_specs(ram):
    specs = {}
    specs['name'] = ram.find('h5', class_ = 'name').text
    size = ram.find('span', class_ = 'size').text
    specs['size'] = re.findall('\d+', size )[0]
    type_mhz = ram.find('span', class_ = 'type').text.split('-')
    specs['type'] = type_mhz[0]
    specs['mhz'] = type_mhz[1]
    kit = ram.find(text = re.compile(r'Kit of \d+'))
    specs['units'] = re.findall('\d+', kit )[0]

    print(specs['name'])
    return specs

def get_hdd_specs(hdd):
    specs = {}
    specs['name'] = hdd.find('h5', class_ = 'name').text
    size = hdd.find('span', class_ = 'size').text
    specs['size'] = re.findall('\d+', size )[0]
    specs['bus'] = 'SATA'
    specs['form_factor'] = '3.5'

    rpm = hdd.find('span', class_ = 'rpm').text
    if 'K' in rpm:
        rpm = rpm.replace('.', '').replace('K', '')
        rpm += '00'
    specs['rpm'] = rpm

    print(specs['name'])
    return specs

def get_ssd_specs(ssd):
    specs = {}
    specs['name'] = ssd.find('h5', class_ = 'name').text
    print(specs['name'])
    size = ssd.find('span', class_ = 'size').text
    specs['size'] = re.findall('\d+', size )[0]
    specs['bus'] = ssd.find('span', class_ = 'bus').text

    form_factor = ssd.find(text = re.compile(r'[SATA|M.2] Format')).replace(' Format', '')
    if form_factor == 'SATA':
        form_factor = '2.5'
    specs['form_factor'] = form_factor
    
    return specs

def get_psu_specs(psu):
    specs = {}
    specs['name'] = psu.find('h1', itemprop = 'name').text
    specs['watts'] = get_spec(psu, 'Watt')
    specs['size'] = get_spec(psu, 'Size')
    specs['efficiency'] = get_spec(psu, 'Efficiency Rating')
    specs['8_cpie_cables'] = get_spec(psu, 'PCI-E cables 8-pin', '0')
    specs['6_cpie_cables'] = get_spec(psu, 'PCI-E cables 6-pin', '0')
    print(specs['name'])
    return specs

def get_cooler_specs(cooler):
    specs = {}
    specs['name'] = cooler.find('h1', itemprop = 'name').text
    specs['supported_sockets'] = get_spec(cooler, 'Supported Sockets').split(', ')
    print(specs['name'])
    return specs

def get_air_cooler_specs(cooler):
    specs = {}
    cooler_common_specs = get_cooler_specs(cooler)
    specs['name'] = cooler_common_specs['name']
    specs['supported_sockets'] = cooler_common_specs['supported_sockets']
    specs['type'] = 'air'
    height = get_spec(cooler, 'Height')
    specs['height'] = re.findall('\d+', height )[0]

    return specs

def get_liquid_cooler_specs(cooler):
    specs = {}
    cooler_common_specs = get_cooler_specs(cooler)
    specs['name'] = cooler_common_specs['name']
    specs['supported_sockets'] = cooler_common_specs['supported_sockets']
    specs['type'] = 'liquid'
    radiator = get_spec(cooler, 'Radiator')
    specs['radiator'] = re.findall('\d+', radiator )[0]
    specs['80_mm_fans'] = get_spec(cooler, '80mm Fans', '0')
    specs['92_mm_fans'] = get_spec(cooler, '92mm Fans', '0')
    specs['120_mm_fans'] = get_spec(cooler, '120mm Fans', '0')
    specs['140_mm_fans'] = get_spec(cooler, '140mm Fans', '0')
    specs['200_mm_fans'] = get_spec(cooler, '200mm Fans', '0')

    return specs

def get_case_specs(case):
    specs = {}
    specs['name'] = case.find('h1', itemprop = 'name').text
    specs['motherboard_size'] = get_spec(case, 'Motherboard', 'ATX')
    specs['psu_size'] = get_spec(case, 'Power Supply', 'ATX')

    width = get_spec(case, 'Width')
    specs['gpu_length'] = re.findall('\d+', width )[0]

    depth = get_spec(case, 'Depth')
    specs['gpu_length'] = re.findall('\d+', depth )[0]

    height = get_spec(case, 'Height')
    specs['gpu_length'] = re.findall('\d+', height )[0]
    
    gpu_length = get_spec(case, 'Supported GPU length')
    specs['gpu_length'] = re.findall('\d+', gpu_length )[0]

    air_cooler_height = get_spec(case, 'Supported GPU length')
    specs['air_cooler_height'] = re.findall('\d+', air_cooler_height )[0]

    specs['120_radiator_support'] = get_spec(case, '120mm Radiator Support', '0')
    specs['140_radiator_support'] = get_spec(case, '140mm Radiator Support', '0')
    specs['240_radiator_support'] = get_spec(case, '240mm Radiator Support', '0')
    specs['280_radiator_support'] = get_spec(case, '280mm Radiator Support', '0')
    specs['360_radiator_support'] = get_spec(case, '360mm Radiator Support', '0')

    specs['2_5_disk_slot'] = get_spec(case, '2.5"', '0')
    specs['3_5_disk_slot'] = get_spec(case, '3.5"', '0')
    print(specs['name'])
    return specs