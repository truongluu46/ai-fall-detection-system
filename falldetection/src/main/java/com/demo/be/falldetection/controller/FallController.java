package com.demo.be.falldetection.controller;

import com.demo.be.falldetection.dto.request.FallRequest;
import com.demo.be.falldetection.service.FallEventService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class FallController {
    FallEventService fallEventService;

    @PostMapping("/fall")
    public String detectFall(@RequestBody FallRequest request){
        fallEventService.handleFall(request.getStatus(), request.getUsername());
        return "OK";
    }
}
