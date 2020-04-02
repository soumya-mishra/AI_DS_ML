###Seaborn:
####Summary:
1.Visualizing statistical relship
2.Plotting with categorical data
3.visualizing the distribution of dataset
4.visualizing linear relationship
 
1.Visualizing statistical relationship:
replot : scatter |line plots   : kind = scatter|line
sns.set(style="darkgrid")
replot : x = , y=,  hue = , data =  , style =     (all are column name except data)
   ci: confidence interval CI
   ci = SD ( spread of distribution )
   
   
   
2.Plotting with categorical data
catplot  : x = ,y =, data =  ,kind =  ,hue = ,
stripplot 
swarmplot
categorical distribution plot : boxplot 
violinplot  -  box plot + Kernel density estimation 
boxenplot   - for large data
Categorical estimate plots:
pointplot
barplot
countplot
 
 
3.visualizing the distribution of dataset 
Univariate distribution :
1.distplot : defsult it draws a histogram with kernel density estimation 
distplot(x, kde=False, rug=True)
bins =20
hist = True/false
 
2. kdeplot                 
Bivariate distribution:
1.joint plot :sns.jointplot(x="x", y="y", data=df);
2.hexbin plot : sns.jointplot(x=x, y=y, kind="hex", color="k");
3.jointplot(x="x", y="y", data=df, kind="kde");
4.pair plot : sns.pairplot(iris);
 
4.visualizing linear relationship:
1.regression model : regplot :(x="total_bill", y="tip", data=tips);
lmplot():sns.lmplot(x="total_bill", y="tip", data=tips);
2. for outliers, it can be useful to fit a robust regression, 
which uses a different loss function to downweight relatively large residuals:
lmplot: x="x", y="y", robust=True, ci = None/SD
 
3.for higher order relationship implot |regplot can fit polynomial regression
lmplot : x="x", y="y",order=2,
        
4.resdiplot : 
for checking whether the simple regression model is appropriate for a dataset
residplot(x="x", y="y", 
 
 
5 . heatmap : correlation 
heatmap(uniform_data, df.corr(), vmin=0, vmax=1,  annot=True)

