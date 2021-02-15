from django.urls import  path
from . import views

urlpatterns = [
    path('api/getLabels', views.get_labels.as_view()),
    path('api/getSectorForSelectedUserID', views.get_sector_for_selected_user_id_api.as_view()),
    path('api/getClientForSelectedUserIDAndSector', views.get_client_for_selected_user_id_and_sector_api.as_view()),
    path('api/getProcessForSelectedClientIDAndSector',views.get_process_for_selected_client_id_and_sector_api.as_view()),
    path('api/getCurrentDatabase', views.get_current_database_api.as_view()),
    path('api/getSubprocessForSelectedClientIDAndProcessID', views.get_subprocess_for_selected_client_id_and_process_id_api.as_view()),
    path('api/getTableDataForSelectedSubProcessID', views.get_table_data_for_selected_sub_process_id.as_view()),
    path('api/getListOfSessionID', views.get_list_of_session_id.as_view()),
    path('api/getSelectTestForSelectedSubprocessID', views.get_select_test_for_selected_subprocess_id.as_view()),
    path('api/getTestParameterForSelectedRuleID', views.get_test_parameter_for_selected_rule_id.as_view()),
    path('api/getCaptionsOfColumnMapping', views.get_captions_of_column_mapping.as_view()),
    path('api/getAllTestList', views.get_all_test_list.as_view()),
    path('api/getColumnMappingForSelectedTable', views.get_column_mapping_for_selected_table.as_view()),
    path('upsert/saveColumnMappingsOnMappingMain', views.save_column_mappings_on_mapping_main.as_view()),
    path('upsert/updateTestParameterDetail', views.update_test_parameter_detail.as_view()),
    path('upsert/updateStatusPendingForSelectedID', views.update_status_pending_for_selected_id.as_view()),
    path('api/getPowerBIURL',views.get_power_bi_url.as_view()),
    path('api/getTableDataForDateRange', views.get_table_data_for_date_range.as_view()),
    path('api/getRiskControlsForSelectedSubprocessId', views.get_risk_controls_for_selected_subprocess_id.as_view())
]