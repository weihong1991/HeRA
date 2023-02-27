from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^HeRA/$', views.index, name='index'),
	url(r'^HeRA/about$', views.about, name='about'),
	url(r'^HeRA/download$', views.download, name='download'),
	url(r'^HeRA/doc$', views.doc, name='doc'),
	url(r'^HeRA/stats$', views.stats, name='stats'),
	url(r'^HeRA/stats/table/$', views.stats_table, name='stats_table'),
	url(r'^HeRA/m1$', views.m1, name='m1'),
	url(r'^HeRA/m2$', views.m2, name='m2'),
	url(r'^HeRA/m3$', views.m3, name='m3'),
	url(r'^HeRA/m4$', views.m4, name='m4'),
	
	# m1 api
	url(r'^HeRA/m1/table/$', view=views.api_m1_table, name='api_m1_table'),
	url(r'^HeRA/m1/plot/$', view=views.api_m1_plot, name='api_m1_plot'),
	# url(r'^apa/m1/plot2/$', view=views.api_m1_plot1, name='api_m1_plot2'),
	# url(r'^apa/m1/table/landscape/$', view=views.api_m1_landscape, name='api_m1_landscape'),
	# url(r'^apa/api/expr/(?P<sid>.*)$', view=views.api_expr, name='api_expr'),
	# url(r'^apa/api/logo_png/(?P<png_name>.*)$', view=views.api_logo_png, name='api_logo_png'),
    url(r'^HeRA/m1/seq_download$', views.api_m1_seq_download, name='api_m1_seq_download'),
	
	# m2 api
	url(r'^HeRA/m2/table/$', view=views.api_m2_table, name='api_m2_table'),
	url(r'^HeRA/m2/plot/$', view=views.api_m2_plot, name='api_m2_plot'),
	# url(r'^apa/api/logo_png/(?P<png_name>.*)$', view=views.api_logo_png, name='api_logo_png'),
	
	# m3 api
	url(r'^HeRA/m3/table1/$', view=views.api_m3_table1, name='api_m3_table1'),
	url(r'^HeRA/m3/table2/$', view=views.api_m3_table2, name='api_m3_table2'),
	url(r'^HeRA/m3/plot/$', view=views.api_m3_plot, name='api_m3_plot'),
	# url(r'^apa/m3/plot2/$', view=views.api_m3_plot2, name='api_m3_plot2'),
	# url(r'^apa/api/logo_png/(?P<png_name>.*)$', view=views.api_logo_png, name='api_logo_png'),
	
	# m4 api
	url(r'^HeRA/m4/table/$', view=views.api_m4_table, name='api_m4_table'),
	url(r'^HeRA/m4/plot/$', view=views.api_m4_plot, name='api_m4_plot'),
	# url(r'^apa/m3/table2/$', view=views.api_m3_table2, name='api_m3_table2'),
	# url(r'^apa/m3/plot1/$', view=views.api_m3_plot1, name='api_m3_plot1'),
	# url(r'^apa/m3/plot2/$', view=views.api_m3_plot2, name='api_m3_plot2'),
	# url(r'^apa/api/logo_png/(?P<png_name>.*)$', view=views.api_logo_png, name='api_logo_png'),
	# plot download
	url(r'^HeRA/download_plot/$', view=views.api_download_plot, name='api_download_plot'),
	url(r'^HeRA/download_data/$', view=views.api_download_data, name='api_download_data'),	

	# gene structure plot api
	# url(r'^apa/gene_structure/$', view=views.api_gene_structure, name='api_gene_structure'),

	# stat api
	# url(r'^apa/api/stats$', views.api_stats, name='api_stats'),

]	
