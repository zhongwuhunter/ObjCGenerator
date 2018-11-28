//
//
//  Created by tiger
//
//

#import "${CLASSNAME}.h"

@interface ${CLASSNAME}()

@property (nonatomic, strong) RACCommand            *refreshCommand;

@end

@implementation ${CLASSNAME}

- (instancetype)init
{
    self = [super init];
    if (self) {
        
    }
    return self;
}


- (RACCommand *)refreshCommand{
    if (!_refreshCommand) {
        _refreshCommand = [[RACCommand alloc] initWithSignalBlock:^RACSignal *(id input) {
            return [[self refreshSignal] doNext:^(id x) {
                NSLog(@"%@", x);
            }];
        }];
    }
    return _refreshCommand;
}




- (RACSignal *)refreshSignal{
    //    return [RACSignal error:[NSError errorWithDomain:@"11" code:-1 userInfo:nil]];
    return [[RACSignal return:[self testData]] delay:0.5];
}


#pragma mark test

- (NSString *)testData{
    return @"测试数据";
}

















@end



