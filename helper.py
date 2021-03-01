#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

F
"""

def load_page(driver):
    search = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, 'OuterDiv'))
    )

    results = driver.find_elements_by_xpath('//*[@id="OuterDiv"]/div')
    slots = int(results[-1].text.split()[-1])
    return slots

def input_field(path, value, driver):
    
    #wait for presence of element to load
    fill_field = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, path))
    )

    #input value
    fill_field.clear()
    time.sleep(1)
    fill_field.send_keys(value)
    fill_field.send_keys(Keys.RETURN)
    time.sleep(1)

def click(path, driver):
    
    #wait for presence of element to load
    box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    
    #click box
    box.click()
    
    time.sleep(1)

def page_load(path, driver):
    #wait for element to be loaded
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, path)))

def fill_out_forms(driver):
    #goes to eligibilty page for ny
    eligible = 'https://am-i-eligible.covid19vaccine.health.ny.gov'
    driver.get(eligible)
        
    
    #waits for text to be loaded
    page_load(eligible_load)
    
    
    #click get started button to go to next page
    try:
        click(get_started)
    except:
        time.sleep(2)
        click(get_started)
    
    
    #fill in dob field
    input_field(dob, '03201935')
    
    
    #click sex option
    click(nb)
    
    
    #click yes for live in ny
    click(live)
    
    
    #click no for work in ny
    click(work)
    
    
    #input zip
    input_field(zipcode, '11554')
    
    
    #click to consent
    try:
        click(consent)
    except:
        time.sleep(2)
        click(consent)

    
    #click to submit
    try:
        click(submit)
    except:
        time.sleep(2)
        click(submit)

    
    #wait for providers page to load
    page_load(providers)
    
    #click to find providers
    click(providers)

    
    #choose site
    try:
        click(jb)
    except:
        time.sleep(2)
        click(jb)
    
    
    #switch to new tab that is opened
    driver.switch_to.window(driver.window_handles[1])