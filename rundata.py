import django
django.setup()
from election import models
from election.data import *
import data

def poll_results():

    # (`result_id`, `lga_name`, `party_abbreviation`, `party_score`, `entered_by_user`, `date_entered`, `user_ip_address`)
    for data in announced_lga_results_data :
        Data = models.Announced_lga_result.objects.create(result_id=data[0],lga_name=data[1],
            party_abbreviation=data[2],party_score=data[3],entered_by_user=data[4],
            date_entered=data[5],user_ip_address=data[6])
        Data.save()
    
    # (`result_id`, `polling_unit_uniqueid`, `party_abbreviation`, `party_score`, `entered_by_user`, `date_entered`, `user_ip_address`)
    for data in announced_pu_results_data :
        Data = models.Announced_pu_result.objects.create(result_id =data[0], polling_unit_unique_id=data[1], party_abbreviation=data[2], 
        party_score=data[3],entered_by_user=data[4], date_entered=data[5],user_ip_address=data[6])
        Data.save()

    # (`uniqueid`, `lga_id`, `lga_name`, `state_id`, `lga_description`, `entered_by_user`, `date_entered`, `user_ip_address`)
    for data in lga_data :
        Data = models.Lga.objects.create(uniqueid =data[0], lga_id=data[1], lga_name=data[2],state_id=data[3],lga_description=data[4],
            entered_by_user=data[5], date_entered=data[6], user_ip_address=data[7])
        Data.save()

# party` (`id`, `partyid`, `partyname`)
    for data in party_data :
        Data = models.Party.objects.create(id =data[0], partyid=data[1], partyname=data[2])
        Data.save()

# `polling_unit` (`uniqueid`, `polling_unit_id`, `ward_id`, `lga_id`, `uniquewardid`, `polling_unit_number`, `polling_unit_name`, `polling_unit_description`, `lat`, `long`, `entered_by_user`, `date_entered`, `user_ip_address`)


    for data in polling_unit_data:
        # if data[11] == None:
        #     data[11] = ''
        Data = models.Polling_unit.objects.create(uniqueid = data[0], polling_unit_id = data[1], ward_id = data[2],
                 lga_id = data[3], uniquewardid = data[4], polling_unit_number = data[5], polling_unit_name = data[6], 
                 polling_unit_description = data[7], lat = data[8], long = data[9], entered_by_user=data[10], 
                 date_entered=data[11], user_ip_address=data[12])
        Data.save()
        
# INSERT INTO `states` (`state_id`, `state_name`) 
    for data in states_data :
        Data = State.objects.create(state_id =data[0], state_name=data[1])
        Data.save()


    # INSERT INTO `ward` (`uniqueid`, `ward_id`, `ward_name`, `lga_id`, `ward_description`, `entered_by_user`, `date_entered`, `user_ip_address`) 
    for data in ward_data :
        Data = Ward.objects.create(uniqueid =data[0], ward_id=data[1], ward_name=data[2], lga_id=data[3],ward_description=data[4],
            entered_by_user=data[5], date_entered=data[6], user_ip_address=data[7])
        Data.save()
    
    # INSERT INTO `agentname` (`name_id`, `firstname`, `lastname`, `email`, `phone`, `pollingunit_uniqueid`) VALUES
    for data in agent_names :
        Data = Agentname.objects.create(name_id =data[0], firstname=data[1], lastname=data[2], email=data[3], 
                phone=data[4], pollingunit_uniqueid=data[5])
        Data.save()
    
    print('finished')
    return {'result': 'update finished'}
poll_results()    
