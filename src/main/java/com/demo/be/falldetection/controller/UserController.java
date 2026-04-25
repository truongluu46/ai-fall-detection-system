package com.demo.be.falldetection.controller;

import com.demo.be.falldetection.dto.request.UserCreationRequest;
import com.demo.be.falldetection.entity.User;
import com.demo.be.falldetection.repositoty.UserRepository;
import com.demo.be.falldetection.service.UserService;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class UserController {
    private final UserRepository userRepository;
    private final UserService userService;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public User createUser(@RequestBody UserCreationRequest request) {
    return userService.createUser(request);
    }
}
