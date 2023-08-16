from django.shortcuts import render,redirect
from django.views import generic
from .models import *
from .data import *
from datetime import datetime

from .forms import AddPollingUnitResultForm,PollingUnitForm,PollResultForm


class GetPollResultView(generic.View):
    template_name = 'index.html'
    def get(self,request,*args,**kwargs):
        form = PollResultForm()
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = PollResultForm(request.POST)
        polling_unit_id =request.POST.get('polling_unit_id')
        query = Announced_pu_result.objects.filter(polling_unit_unique_id=polling_unit_id)

        if query.exists():
            context = {'form':form,'query':query}
            return render(request,'index.html',context)

        err_msg = 'No result available for the selected Polling Unit'
        context = {'err_msg':err_msg,'form':form}
        return render(request,'index.html',context)

class ResultSumTotalView(generic.View):
    template_name = 'result.html'
    def get(self,request,*args,**kwargs):
        form = PollingUnitForm()

        context = {'form':form}
        return render(request,'result.html',context)

    def post(self,request,*args,**kwargs):
        form = PollingUnitForm(request.POST)
        lga_id = request.POST.get('polling_unit_unique_id')
        polling_units = Polling_unit.objects.filter(lga_id=lga_id) # Get all polling units under a specific lga
        if polling_units.exists():
            total = 0

            for poll_unit in polling_units:
                #  get id of each polling unit under the polling units
                poll_unit_id = Poll_unit.polling_unit_id
                
                # check results of each polling unit
                poll_unit_result = Announced_pu_result.objects.filter(polling_unit_unique_id=poll_unit_id)
                if poll_unit_result.exists():

                    # loop through each result and add up to total
                    for party in poll_unit_result:
                        total += int(party.party_score)
            context = {'form':form,'total':total,'unit':lga_id}
            return render(request,self.template_name,context)
        
        context = {'form':form,'err_msg':'There is no result for this lga'}
        return render(request,'result.html',context)        

class UploadPostResult(generic.View):
    template_name = 'add_poll.html'
    def get(self,request,*args,**kwargs):
        form = AddPollingUnitResultForm()
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = AddPollingUnitResultForm(request.POST)
        polling_unit_unique_id = request.POST.get('polling_unit_unique_id')
        party_abbreviation = request.POST.get('party_abbreviation')
        party_score = request.POST.get('party_score')
        entered_by_user = request.POST.get('entered_by_user')
        date_entered = datetime.now()
        user_ip_address = request.POST.get('user_ip_address')
        if form.is_valid():
            query = Announced_pu_result.objects.create(polling_unit_unique_id = polling_unit_unique_id, party_abbreviation = party_abbreviation, 
                            party_score = party_score, entered_by_user = entered_by_user,date_entered = date_entered,
                            user_ip_address = user_ip_address)
            query.save()
            context = {'message':'Poll Result Updated Successfully','form':form}
            return render(request,'add_poll.html',context)

        context = {'err_msg':'There was an error updating the result. Please try again','form':form}
        return render(request,self.template_name,context)
        
