import json

class JsonChart: 
  
  
  
  class DateChart: 

    class DataSet: 
      data = [1,2,3,4,5,6,7,8,9,]
      label =  "Expense"
      backgroundColor = 'rgba(0,200,155,.35)'
      borderColor = 'rgba(0,200,155,0.60)'
      borderWidth = 1
      pointStyle = 'circle'
      pointRadius =  2
      pointBorderColor  = 'transparent'
      pointBackgroundColor  =  'rgba(0,200,155,0.60)'
       
   
      def getJson(self): 
        temp = { 
         'data'                : self.data ,    
         'label'               : self.label ,
         'backgroundColor'     : self.backgroundColor,
         'borderColor'         : self.borderColor,
         'borderWidth'         : self.borderWidth ,
         'pointStyle'          : self.pointStyle,
         'pointRadius'         : self.pointRadius,
         'pointBorderColor'    : self.pointBorderColor,
         'pointBackgroundColor': self.pointBackgroundColor,
       
         }
     
        return temp 
 
      
    labels = [ "1390", "1391", "1392",  "1397", "1398", "1399", "1400" , "1401" ]
    typeTem = 'line'
    defaultFontFamily =   'Montserrat' 
    datasets =[DataSet(),DataSet()]
    def getJson(self): 
      dat = []
      for d in self.datasets: 
       dat.append(d.getJson())
      
      date = {
       'labels'             : self.labels, 
       'type'               : self.typeTem,
       'defaultFontFamily'  : self.defaultFontFamily , 
       'datasets'           : [self.datasets[0].getJson(),self.datasets[1].getJson()]
        }
      return date
       
  class OptionsChart: 
   
   def getJson(self): 
       
    options = {
            'responsive': True,
            'tooltips': {
                'mode': 'index',
                'titleFontSize': 12,
                'titleFontColor': '#000',
                'bodyFontColor': '#000',
                'backgroundColor': '#fff',
                'titleFontFamily': 'Montserrat',
                'bodyFontFamily': 'Montserrat',
                'cornerRadius': 3,
                'intersect': False,
            },
            'legend': {
                "display": False,
                'position': 'top',
                'labels': {
                    'usePointStyle': True,
                    'fontFamily': 'Montserrat',
                },


            },
            'scales': {
                'xAxes': [ {
                    'display': True,
                    'gridLines': {
                        'display': False,
                        'drawBorder': False
                    },
                    'scaleLabel': {
                        'display': False,
                        'labelString': 'Month'
                    }
                        } ],
                'yAxes': [ {
                    'display': True,
                    'gridLines': {
                        'display': False,
                        'drawBorder': False
                    },
                    'scaleLabel': {
                        'display': True,
                        'labelString': 'Value'
                    }
                        } ]
            },
            'title': {
                'display': False,
            }
        }
        



    return options
  

  typeChart = 'line'
  dataChart    =  DateChart()
  optionsChart =  OptionsChart()
  

  def getJson(self):
    temp = {
      'type'    :   self.typeChart  ,
      'data'    :   self.dataChart.getJson(),
      'options' :   self.optionsChart.getJson()
    }
    return temp 
  


  ########################## config chart    
  def setConfighChart(self ,configh , number):
    try : 
      data = configh['data'] 
      self.dataChart.datasets[number-1].data = data
    except : 
      pass
    
    try : 
      label = configh['label'] 
      self.dataChart.datasets[number-1].label = label
    except : 
      pass

    try : 
      backgroundColor = configh['backgroundColor'] 
      self.dataChart.datasets[number-1].backgroundColor = backgroundColor
    except : 
      pass

    try : 
      borderWidth = configh['borderWidth'] 
      self.dataChart.datasets[number-1].borderWidth = borderWidth
    except : 
      pass


    try : 
      borderColor = configh['borderColor'] 
      self.dataChart.datasets[number-1].borderColor = borderColor
    except : 
      pass

    try : 
      pointStyle = configh['pointStyle'] 
      self.dataChart.datasets[number-1].pointStyle = pointStyle
    except : 
      pass


    try : 
      pointRadius = configh['pointRadius'] 
      self.dataChart.datasets[number-1].pointRadius = pointRadius
    except : 
      pass


    try : 
      pointBorderColor = configh['pointBorderColor'] 
      self.dataChart.datasets[number-1].pointBorderColor = pointBorderColor
    except : 
      pass

    try : 
      pointBackgroundColor = configh['pointBackgroundColor'] 
      self.dataChart.datasets[number-1].lapointBackgroundColorbel = pointBackgroundColor
    except : 
      pass




      




  def setChartName(self,label,number):
    self.dataChart.datasets[number].label = label
        
  def setChartDate(self , dataTemp , number ):
    self.dataChart.datasets[number-1].data = dataTemp
  
  def setLabel(self,labels):
    self.dataChart.labels = labels
 
  
    
  


