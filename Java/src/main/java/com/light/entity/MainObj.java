package com.light.entity;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonIgnore;

@Entity
@Table(name = "main")
public class MainObj {
    @Id
    private Long id;

    @Column(name = "datetime")
    private Date datetime;

    private String radiance;

    private int pixels;

    private int cityId;

    private String window;

    @JsonIgnore
    private String file;

    public Date getDatetime() {
        return datetime;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
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

    public int getCityId() {
        return cityId;
    }

    public void setCityId(int cityId) {
        this.cityId = cityId;
    }

    public int getPixels() {
        return pixels;
    }

    public void setPixels(int pixels) {
        this.pixels = pixels;
    }

    public String getRadiance() {
        return radiance;
    }

    public void setRadiance(String radiance) {
        this.radiance = radiance;
    }

    public void setDatetime(Date datetime) {
        this.datetime = datetime;
    }
 
}
