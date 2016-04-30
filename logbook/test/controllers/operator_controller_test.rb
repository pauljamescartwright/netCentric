require 'test_helper'

class OperatorControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get operator_index_url
    assert_response :success
  end

  test "should get show" do
    get operator_show_url
    assert_response :success
  end

  test "should get new" do
    get operator_new_url
    assert_response :success
  end

  test "should get create" do
    get operator_create_url
    assert_response :success
  end

  test "should get edit" do
    get operator_edit_url
    assert_response :success
  end

  test "should get update" do
    get operator_update_url
    assert_response :success
  end

  test "should get destroy" do
    get operator_destroy_url
    assert_response :success
  end

end
