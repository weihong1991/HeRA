# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Load modules
import base64
import os
import json
import commands
import subprocess
import pickle
import re
import csv

# resources and rscripts

rcommand = commands.getoutput("which Rscript")
#rcommand = "C:/Program Files/R/R-3.5.1/bin/Rscript.exe"
root_path = os.path.dirname(os.path.abspath(__file__))
print ("#########################")
print (root_path)
rscript_dir = os.path.join(root_path, 'rscripts')
resource_jsons = os.path.join(root_path, 'resource', 'jsons')
resource_pngs = os.path.join(root_path, 'resource', 'pngs')
resource_logo = os.path.join(resource_pngs, 'logo')
resource_data = os.path.join(root_path, 'resource', 'data_20200331')
# def test(request):
 	# title = "test page"
 	# context = {"title": title}
 	# return HttpResponse("This is a test page")
	
def index(request):
	title = "HeRA Homepage"
	context = {"title": title}
		
	return render(request=request, template_name="HeRA/index.html", context=context, status=200)

def about(request):
	title = "HeRA Contact"
	context = {"title": title}

	return render(request, "HeRA/about.html", context, status=200)

def download(request):
	title = "HeRA Downloads"
	context = {"title": title}

	return render(request, "HeRA/download.html", context, status=200)

def doc(request):
	title = "HeRA Documents"
	context = {"title": title}

	return render(request, "HeRA/Manual.html", context, status=200)

def stats(request):
	title = "HeRA Dataset"
	context = {"title": title}

	return render(request, "HeRA/statistics.html", context, status=200)

def m1(request):
 	title = "HeRA Expression"
 	context = {"title": title}

 	return render(request, "modules-eRNA/m1.html", context, status=200)
	
def m2(request):
 	title = "HeRA Trait Relevance"
 	context = {"title": title}
 	return render(request, "modules-eRNA/m2.html", context, status=200)
	
def m3(request):
 	title = "HeRA Regulation"
 	context = {"title": title}

 	return render(request, "modules-eRNA/m3.html", context, status=200)

def m4(request):
 	title = "HeRA TargetGenes"
 	context = {"title": title}

 	return render(request, "modules-eRNA/m4.html", context, status=200)

def api_m1_table(request):
	title = "API | m1_table"
	context = {"title": title}
	tissue_id = request.GET.getlist('tissue_id[]')
	#print tissue_id
	pos_id = request.GET['pos_id']
	e_id = request.GET['e_id']
	g_id = request.GET['g_id'] # get parameters from ajax
	if(len(tissue_id)==0):
		tissue_id = "0"
	else:
		tissue_id = ".".join(tissue_id)
	info_join = "##".join([tissue_id, pos_id, e_id, g_id]) # join by ## to avoid empty parameter
	#sample_size = request.GET['sample_size']
	rscript = os.path.join(rscript_dir, "api_m1_table.R")
	cmd = [rcommand, rscript, root_path, info_join]
	print cmd
	json_file = os.path.join(resource_jsons, "".join(["m1/eRNA_m1_",info_join, "_table_all.json"]))
	#print (json_file)
	if not os.path.exists(json_file):
		subprocess.check_output(cmd, universal_newlines=True)
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)
	
def api_m1_plot(request):
	title = "API | m1_plot"
	context = {"title": title}
	
	eRNA_ID = request.GET['eRNA_ID']
	tissue = request.GET['Tissue']
	file = request.GET['file']
	#sample_size = request.GET['Sample_size_limit']
	rscript = os.path.join(rscript_dir, "api_m1_plot.R")
	cmd = [rcommand, rscript, root_path, tissue, eRNA_ID,file]
	png_file = os.path.join(resource_pngs,"m1", ".".join(["HeRA_m1", tissue, eRNA_ID,"png"]))
	if not os.path.exists(png_file):
		subprocess.check_output(cmd, universal_newlines=True)
 	with open(png_file,'rb') as f:
 		return HttpResponse(base64.b64encode(f.read()), content_type="image/png")
        
def api_m1_seq_download(request):
	title = "API | m1_seq_download"
	context = {"title": title}
	#module = request.GET ['module']
	file = request.GET['file']
	plot_file = os.path.join(resource_data,"genome/sequences",file)
	#print (plot_file)
	
	response = HttpResponse(open(plot_file,'r'),content_type='text/plain')
	response['Content-Disposition'] = "".join(["attachment; filename=",file])
	return response
	
def api_m2_table(request):
	title = "API | m2_table"
	context = {"title": title}
	tissue_id = request.GET.getlist('tissue_id[]')
	pos_id = request.GET['pos_id']
	e_id = request.GET['e_id']
	g_id = request.GET['g_id'] # get parameters from ajax
	if(len(tissue_id)==0):
		tissue_id = "0"
	else:
		tissue_id = ".".join(tissue_id)
	info_join = "##".join([tissue_id, pos_id, e_id, g_id]) # join by ## to avoid empty parameter
	#sample_size = request.GET['sample_size']
	rscript = os.path.join(rscript_dir, "api_m2_table.R")
	cmd = [rcommand, rscript, root_path, info_join]
	print cmd
	json_file = os.path.join(resource_jsons, "".join(["m2/eRNA_m2_",info_join, "_table_all.json"]))
	#print (json_file)
	if not os.path.exists(json_file):
		subprocess.check_output(cmd, universal_newlines=True)
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)

def api_m2_plot(request):
	title = "API | m2_plot"
	context = {"title": title}
	query_tissues = request.GET["Tissue"]
	e_id = request.GET['eRNA_ID']
	trait = request.GET['trait']
	
	#sample_size = request.GET['Sample_size_limit']
	trait2=trait.replace("btn_","")
	FDR= trait2+"_FDR"
	# test=trait2+"_test"
	FDR=request.GET[FDR]
	# test=request.GET[test]
	# print pv
	# print FDR
	# print test
	
	rscript = os.path.join(rscript_dir, "api_m2_plot.R")
	cmd = [rcommand, rscript, root_path, query_tissues, e_id,trait2,FDR]
	png_file = os.path.join(resource_pngs,"m2", ".".join(["eRNA_m2", query_tissues, e_id, trait2, "png"]))
	if not os.path.exists(png_file):
		subprocess.check_output(cmd, universal_newlines=True)
	
 	with open(png_file,'rb') as f:
 		return HttpResponse(base64.b64encode(f.read()), content_type="image/png")

def api_m3_table1(request):
	title = "API | m3_table1"
	context = {"title": title}
	tissue_id = request.GET.getlist('tissue_id[]')
	#print tissue_id
	pos_id = request.GET['pos_id']
	e_id = request.GET['e_id']
	g_id = request.GET['g_id'] # get parameters from ajax
	if(len(tissue_id)==0):
		tissue_id = "0"
	else:
		tissue_id = ".".join(tissue_id)
	info_join = "##".join([tissue_id, pos_id, e_id, g_id]) # join by ## to avoid empty parameter
	#sample_size = request.GET['sample_size']
	rscript = os.path.join(rscript_dir, "api_m3_table1.R")
	cmd = [rcommand, rscript, root_path, info_join]
	print cmd
	json_file = os.path.join(resource_jsons, "".join(["m3/eRNA_m3_",info_join, "_table1_all.json"]))
	#print (json_file)
	if not os.path.exists(json_file):
		subprocess.check_output(cmd, universal_newlines=True)
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)
	
def api_m3_table2(request):
	title = "API | m3_table2"
	context = {"title": title}
	tissue = request.GET['tissue']
	id = request.GET['id']
	rscript = os.path.join(rscript_dir, "api_m3_table2.R")
	cmd = [rcommand, rscript, root_path, tissue, id]
	#cmd1 = " ".join([rcommand, rscript, root_path, data_id, query_tissues, gene_id])
	#commands.getoutput(cmd1)
	json_file = os.path.join(resource_jsons, "".join(["m3/eRNA_m3_",tissue,"_",id,"_table2_all.json"]))
	if not os.path.exists(json_file):
		subprocess.check_output(cmd, universal_newlines=True)
	#return HttpResponse("data_id = " + data_id + ";query_tissues = " + query_tissues + ";gene_id = " + gene_id )
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)

def api_m3_plot(request):
	title = "API | m3_plot"
	context = {"title": title}
	
	t_id = request.GET['tis2']
	e_id = request.GET['eRNA']
	g_id = request.GET['Symbol']
	
	#sample_size = request.GET['Sample_size_limit']
	rscript = os.path.join(rscript_dir, "api_m3_plot.R")
	cmd = [rcommand, rscript, root_path, t_id, e_id, g_id]
	png_file = os.path.join(resource_pngs,"m3", ".".join(["HeRA_m3", t_id,e_id,g_id,"png"]))
	if not os.path.exists(png_file):
		subprocess.check_output(cmd, universal_newlines=True)
 	with open(png_file,'rb') as f:
 		return HttpResponse(base64.b64encode(f.read()), content_type="image/png")

def api_m4_table(request):
	title = "API | m4_table"
	context = {"title": title}
	tissue_id = request.GET.getlist('tissue_id[]')
	#print tissue_id
	pos_id = request.GET['pos_id']
	e_id = request.GET['e_id']
	g_id = request.GET['g_id'] # get parameters from ajax
	if(len(tissue_id)==0):
		tissue_id = "0"
	else:
		tissue_id = ".".join(tissue_id)
	info_join = "##".join([tissue_id, pos_id, e_id, g_id]) # join by ## to avoid empty parameter
	#sample_size = request.GET['sample_size']
	rscript = os.path.join(rscript_dir, "api_m4_table.R")
	cmd = [rcommand, rscript, root_path, info_join]
	print cmd
	json_file = os.path.join(resource_jsons, "".join(["m4/eRNA_m4_",info_join, "_table_all.json"]))
	#print (json_file)
	if not os.path.exists(json_file):
		subprocess.check_output(cmd, universal_newlines=True)
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)
	
def api_m4_plot(request):
	title = "API | m4_plot"
	context = {"title": title}
	tissue = request.GET['tis2']
	e_ID = request.GET['eRNA']
	g_ID = request.GET['Symbol']
	#file = request.GET['file']
	#sample_size = request.GET['Sample_size_limit']
	rscript = os.path.join(rscript_dir, "api_m4_plot.R")
	cmd = [rcommand, rscript, root_path, tissue, e_ID, g_ID]
	png_file = os.path.join(resource_pngs,"m4", ".".join(["HeRA_m4", tissue, e_ID, g_ID ,"png"]))
	if not os.path.exists(png_file):
		subprocess.check_output(cmd, universal_newlines=True)
 	with open(png_file,'rb') as f:
 		return HttpResponse(base64.b64encode(f.read()), content_type="image/png")		

		
def api_download_plot(request):
	title = "API | download_plot"
	context = {"title": title}
	module = request.GET ['module']
	file = request.GET['file']
	plot_file = os.path.join(resource_pngs, module,file)
	#print (plot_file)
	
	response = HttpResponse(open(plot_file,'r'),content_type='application/pdf')
	response['Content-Disposition'] = "".join(["attachment; filename=",file])
	return response
	
def api_download_data(request):
	title = "API | download_data"
	context = {"title": title}
	module = request.GET ['module']
	file = request.GET['file']
	data_file = os.path.join(resource_pngs,module,file)
	print (file)
	
	response = HttpResponse(open(data_file,'r'),content_type='text/csv')
	response['Content-Disposition'] = "".join(["attachment; filename=",file])
	return response
	
	
def stats_table(request):
	title = "HeRA stat table"
	context = {"title": title}
	json_file = os.path.join(resource_data,"Summary.json")
	data = json.load(open(json_file, 'r'))
	return JsonResponse(data, safe=False)