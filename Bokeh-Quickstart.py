#!/usr/bin/env python
# coding: utf-8

# In[13]:


# The basic steps to creating plots with the bokeh.plotting interface are:

# Prepare some data

#     In this case plain python lists, but could also be NumPy arrays or Pandas series.
# Tell Bokeh where to generate output

#     In this case using output_file(), with the filename "lines.html". Another option is output_notebook() for use in Jupyter notebooks.
# Call figure()

#     This creates a plot with typical default options and easy customization of title, tools, and axes labels.
# Add renderers

#     In this case, we use line() for our data, specifying visual customizations like colors, legends and widths.
# Ask Bokeh to show() or save() the results.

#     These functions save the plot to an HTML file and optionally display it in a browser.


# In[14]:


from bokeh.plotting import figure, output_file, show


# In[15]:


#dummy data
x = [1,2,3,4,5]
y = [6,7,2,4,5]


# In[16]:


#output to static HTML file
output_file("lines.html")


# In[17]:


#create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')


# In[18]:


#add a line renderer with legend and line thickness
p.line(x,y,legend="Temp.", line_width=2)


# In[19]:


show(p)


# In[ ]:




