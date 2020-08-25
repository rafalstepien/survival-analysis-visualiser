mnm_color_pallete = {"mnm_blue":"#27384A", 
                     "mnm_green":"#48C095",  
                     "mnm_grey":"#B6B6B6", 
                     "mnm_lightgrey":"#ECECEC",  
                     "mnm_text":"#5F5F5F", 
                     "PCBB_burgundy":"#BC0020"
                     }

fig_height = 700
border_color = mnm_color_pallete["mnm_blue"]
background_color = mnm_color_pallete["mnm_grey"]
font_color = mnm_color_pallete["mnm_blue"]
components_color = mnm_color_pallete["mnm_lightgrey"]

graph_height = '600px'
padding = '10px 10px 10px 10px'
border_radius = 5
margin = 5

background_style = {
                'backgroundColor': background_color
                }

graph_style = {'marginLeft': margin, 'marginRight': margin, 'marginTop': margin, 'marginBottom': margin,
               'padding': padding,
               'backgroundColor': components_color,
               'height': graph_height,
               'border-radius': border_radius,
               'border': f'2px {border_color} solid'
               }

body_style = {'marginLeft': margin, 'marginRight': margin, 'marginTop': margin, 'marginBottom': margin,
            #   'backgroundColor': background_color,
              'padding': padding
              }

section_style = {'marginLeft': margin, 'marginRight': margin, 'marginTop': margin, 'marginBottom': margin,
               'padding': padding,
               'border-radius': border_radius,
               'backgroundColor': components_color,
               'border': f'2px {border_color} solid',
                }

navbar_style = {'marginLeft': margin, 'marginRight': margin, 'marginTop': margin, 'marginBottom': margin,
                'padding': padding,
                'backgroundColor': components_color,
                'border-radius': border_radius,
                'border': f'2px {border_color} solid'
                }
