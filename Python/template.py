v_url =  {'root':'http://ocicatmedia.github.io/'}
nav = {
	'site':[['Home',''],['Portfolio','portfolio'],['Contact','contact'],['About','about']],
	'home':[['Latest News','#news'],['Archived News','news']]
	}
template = {}

def site_nav (active):
	nav_site = []
	nav_return = ''

	for i in nav['site']:
		nav_site.append('<a href="' + v_url['root'] + i[1] + '/">' + i[0] + '</a>')
		if (i[0] == active):
			nav_site[-1] = '<li class="active">' + nav_site[-1] + '</li>'
		else:
			nav_site[-1] = '<li>' + nav_site[-1] + '</li>'
	
	for i in nav_site:
		nav_return = nav_return + i
	
	nav_return = '<ul>' + nav_return + '</ul>'
	
	return nav_return
	
	
def page_nav (page,active):
	nav_page = []
	nav_return = ''

	for i in nav[page]:
		if (i[1][0] == "#"):
			nav_page.append('<a href="' + i[1] + '">' + i[0] + '</a>')
		else:
			nav_page.append('<a href="' + v_url['root'] + i[1] + '/">' + i[0] + '</a>')
		
		if (i[0] == active):
			nav_page[-1] = '<li class="active">' + nav_page[-1] + '</li>'
		else:
			nav_page[-1] = '<li>' + nav_page[-1] + '</li>'
	
	for i in nav_page:
		nav_return = nav_return + i
	
	nav_return = '<ul>' + nav_return + '</ul>'
	
	return nav_return

#nav_page = {'index'['Home',''],['Portfolio','portfolio'],['Contact','contact'],['About','about']]


#<a href="#ocicatmedia">OciCat Media</a>
#<a href="#matthewmoore">Matthew Moore</a>
#<a href="#theocicat">The OciCat</a>
