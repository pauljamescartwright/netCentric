require 'test_helper'

class SpecialEventControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get special_event_index_url
    assert_response :success
  end

  test "should get show" do
    get special_event_show_url
    assert_response :success
  end

  test "should get new" do
    get special_event_new_url
    assert_response :success
  end

  test "should get create" do
    get special_event_create_url
    assert_response :success
  end

  test "should get edit" do
    get special_event_edit_url
    assert_response :success
  end

  test "should get update" do
    get special_event_update_url
    assert_response :success
  end

  test "should get destroy" do
    get special_event_destroy_url
    assert_response :success
  end

end
