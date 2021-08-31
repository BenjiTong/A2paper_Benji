package com.light.model;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class MainObject {
  @Id
  @GeneratedValue(strategy=GenerationType.IDENTITY)
  private Integer id;

  private Date dateTime;

  private Float radiance;

  private Long pixels;

  private Integer cityId;

  private String window;

  private String file;

  public Integer getId() {
    return id;
  }

  public String getFile() {
    return file;
  }

  public void setFile(String file) {
    this.file = file;
  }

  public String getWindow() {
    return window;
  }

  public void setWindow(String window) {
    this.window = window;
  }

  public Integer getCityId() {
    return cityId;
  }

  public void setCityId(Integer cityId) {
    this.cityId = cityId;
  }

  public Long getPixels() {
    return pixels;
  }

  public void setPixels(Long pixels) {
    this.pixels = pixels;
  }

  public Float getRadiance() {
    return radiance;
  }

  public void setRadiance(Float radiance) {
    this.radiance = radiance;
  }

  public Date getDateTime() {
    return dateTime;
  }

  public void setDateTime(Date dateTime) {
    this.dateTime = dateTime;
  }

  public void setId(Integer id) {
    this.id = id;
  }
 

 
}